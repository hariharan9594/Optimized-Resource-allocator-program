import pandas as pd

print("Please Enter the units and hours:")
#Reading input data from User

unit = int(input(""))
hour = int(input(""))

# Reading Data from CSV file
data = pd.read_csv('local.csv')
New_cost = data['New York'].tolist()
New_cost.reverse()
India_cost = data['India'].tolist()
India_cost.reverse()
China_cost = data['China'].tolist()
China_cost.reverse()
capacity = data['capacity'].tolist()
capacity.reverse()
machines = data['machines'].tolist()
machines.reverse()

class Analyse:
    ny_ls = []
    ind_ls =[]
    ch_ls =[]
    total = 0
    ny_m_ls =[]
    ind_m_ls =[]
    ch_m_ls=[]
    def __init__(self, country):
        self.country = country
    
    # Method to calculate total cost and add allocated machines to list
    def cost(self, quan,cap):
        ind = capacity.index(cap)
        self.total = New_cost[ind]*quan + self.total 
        if quan !=0:
            ms = tuple((machines[ind], quan))
            if self.country == "NewYork":
                self.ny_m_ls.append(ms)
            elif self.country == "India":
                self.ind_m_ls.append(ms)
            elif self.country == "China":
                self.ch_m_ls.append(ms)
        else:
            pass

    # This method allocates Machines based on unit and capacity
    # Recursion is used to allocate machines by analysing units and capacity passing as arguments

    def allocate_machines(self, unit,cap,st):
        if unit>0:
            if self.country == "NewYork":
                st=unit//cap
                self.cost(st,cap)
                self.ny_ls.append(st)
                self.allocate_machines(unit%cap, cap/2, st)
            elif self.country =="India":
                if cap != 20:
                    st=unit//cap
                    self.cost(st,cap)
                    self.ind_ls.append(st)
                    self.allocate_machines(unit%cap, cap/2, st)
                else:
                    self.allocate_machines(unit, cap/2, st)
            elif self.country =="China":
                if cap != 40 and cap != 320:
                    st=unit//cap
                    self.cost(st,cap)
                    self.ch_ls.append(st)
                    self.allocate_machines(unit%cap, cap/2, st)
                else:
                    self.allocate_machines(unit, cap/2, st)
    # This method returns output in dictionary format
    def Print_data(self, h):
        new_dic = {}
        new_dic["region"] = self.country
        new_dic["total_cost"] = "$"+str(self.total*h)
        if self.country == "NewYork":
            new_dic["machines"] = self.ny_m_ls
        elif self.country == "India":
            new_dic["machines"] = self.ind_m_ls
        elif self.country == "China":
            new_dic["machines"] = self.ch_m_ls
        return new_dic

# main program
out = []
#Three objects created using class Analyse
newyork = Analyse("NewYork")
india = Analyse("India")
china = Analyse("China")
newyork.allocate_machines(unit,capacity[0],0)
d1 = newyork.Print_data(hour)
out.append(d1)
india.allocate_machines(unit,capacity[0],0)
d2 = india.Print_data(hour)
out.append(d2)
china.allocate_machines(unit,capacity[0],0)
d3 = china.Print_data(hour)
out.append(d3)
out_dic = {}
# add output to out_dic
out_dic["Output"] = out
# final output in dictionary format
print(out_dic)