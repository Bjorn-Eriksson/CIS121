#Created by Bjorn Erikson

############# Day 1: Deep dive into 'self' in python  ################
#Also check W10, D1 of notebook for images

#The instance variables of an object can differ by copies(instances) of that object
# and as a result all need their own space in memory.
#However, since all the methods do the same thing (just on different values of the instance variables)
# they can share space in memory.

#When we define a class, the name of that class is added to the current namespace with a refernece
# to a class definition object. 
#. Anytime we try to do 'planet stuff' python first checks for this reference using the instance variable
#.  __class__ which references the class definiton object.

#Build a star class that takes a name as an argument and 
# has a getter, a setter, and a string representation of the object.
# Then instantiate an instance of the Star.

class Star:
    def __init__(self, name, radius, mass, temperature):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.temperature = temperature
    
    #GETTERS 
    def get_name(self):
        return self.name
    def get_radius(self):
        return self.radius
    def get_mass(self):
        return self.mass
    def get_temperature(self):
        return self.temperature
    
    #SETTERS
    def set_name(self, new_name):
        self.name = new_name
    def set_radius(self, new_radius):
        self.radius = new_radius
    def set_mass(self, new_mass):
        self.mass = new_mass
    def set_temperature(self, new_temperature):
        self.temperature = new_temperature
    
    #String representation of objet
    def __str__(self):
        message = ''
        message += f'Hello, my name is {self.name}. I am a star!'
        return message

star1 = Star('Ganymede', 12500, 850201, 5500)

print(star1)




































































