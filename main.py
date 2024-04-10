class Cars():

    def __init__(self, name, color, cost, size, year, type, city):

        self.ism = name
        self.rangi = color
        self.narxi = cost
        self.hajmi = size
        self.yili = year
        self.turi = type
        self.ish_shahri = city



    def get_name(self):
        return self.ism
    
    def get_color(self):
        return self.rangi
    
    def get_cost(self):
        return self.narxi
    
    def get_size(self):
        return self.hajmi
    
    def get_year(self):
        return self.yili
    
    def get_type(self):
        return self.turi
    
    def get_city(self):
        return self.ish_shahri
    
    


    def set_name(self, new_name):
        self.ism = new_name

    def set_color(self, new_color):
        self.rangi = new_color

    def set_cost(self, new_cost):
        self.narxi = new_cost
        
    def set_size(self, new_size):
        self.hajmi = new_size
 
    def set_year(self, new_year):
        self.yili = new_year

    def set_type(self, new_type):
        self.turi = new_type

    def set_city(self, new_city):
        self.ish_shahri = new_city
        


    def info(self):
        allname = f"name: {self.ism} ,  color: {self.rangi} ,  cost: {self.narxi} ,   size:{self.hajmi} ,  year: {self.yili},  type: {self.turi} ,  city: {self.ish_shahri}"
        return allname

    
    

common = Cars("BMW", "black","100000$","average","2023","elektonika", "AQSH")

common.set_name("BMW")
common.set_color("black")
common.set_cost("1000000$")
common.set_size("average")
common.set_year("2023")
common.set_type("elaktronika")
common.set_city("AQSH")


print(common.info())