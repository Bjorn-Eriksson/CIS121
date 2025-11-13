#Created by Bjorn Eriksson

class Monster:
    #Name
    #Size
    #Num of teeth
    #Power

    def __init__(self, name):
        self.name = name
        self.size = 0
        self.num_of_teeth = -1
        self.power = -1
        

    #Getters
    def get_name(self):
        return self.name
    
    def get_size(self):
        return self.size
    
    def get_num_of_teeth(self):
        return self.num_of_teeth
    
    def get_power(self):
        return self.power


    #Setters
    def set_size(self, value):
        if value > 0:
            self.size = value
    
    def set_num_of_teeth(self, value):
        if value >= 0:
            self.num_of_teeth = value

    def set_power(self, value):
        if value > 0:
            self.power = value

    
    def scare(self):
        if self.power > 50:
            return "Very scary!"
        elif self.power < 10:
            return "Not spooky at all."
        elif 10 < self.power < 50:
            return "Moderately spooky monster."
    
    def __str__(self): #Allows us to print whatever is inside this class & their methods when we call it.
        return f"{self.get_name()} Size: {self.get_size()} LBS, Power: {self.get_power()}. It also has {self.get_num_of_teeth()} teeth so it is {self.scare()}"

#Instantiating Monsters
monster1 = Monster("Krish")
monster1.set_num_of_teeth(30)
monster1.set_power(1)
monster1.set_size(0.1)

#print(monster1)













































