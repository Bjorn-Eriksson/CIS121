#Created by Bjorn Eriksson

################## Day 1: Object Oriented Programming & Classes ######################

#What is a dog? What can it do?
#These traits can be applied to OOP.

dog1_name = 'gus'
dog1_age = 7
dog1_weight = 82
dog1_breed = 'rottski'
dog1_size = 'medium'

#We are going to study object oritnetd programming (OOP).
#OOP is about objects, the individual data items that are manipulated
#to solve a problem. In python, every data item is an object.

#In order to understand objects, we need to understand classes.
#In OOP, classes are used to describe what an object 'looks' like.
#That meaning, classes are the blueprints of an object.

#Recall, everything in python is an object. An int is an object. The
#Integer (object) 3 is an instance of the int class.
#That means there is a class caleed int that will describe what
#an int looks like and what it can do.
#One of the things it can do it called __add__(), that is _ _(add)_ _

numx = 2
numx = numx.__add__(3)
#The result is num = 5
#The + symbol is an alias for __add__()

#over the next few lessons, we will build a model of our solar system.
#To start, let's build a simple representaion of a planet and design
#a class (design a blueprint).

#The general format of a class looks like;

#class Classname:
    #def method1():
        #block of code
    #def method2():
        #block of code
    #Methods are functions that are specifically associated within a class.

#When defining classes, we use a different way to spell them compared
# to functions
#def my_fctn_has_many_names():
#def ThisClassHasManyNames():


#The first method that many classes have is called a constructor.
#Which defined the way the object is created. The constructor 
#frequently creates instance variables to fold these values.

#In python, the constructor is always called __init__().

#In python, each method requires one special parameter
#(the first parameter)
#which refers to the object that is being created.

#Let's see an example of a planet class that has 
# 1.  name
# 2.  radius
# 3.  mass
# 4.  distance

class Planet:
    def __init__(self, _name):
        self.name = _name

planet1 = Planet('X25')
planet2 = Planet('Z37')



class Dog:
    def __init__(self, name, age, weight, breed, size):
        self.name = name 

dog1 = Dog('Gus', 7, 82, 'rottski', 'medium')
dog2 = Dog('Nala', 7, 71, 'rottski', 'medium')
#######################################################################################
# Day 2: Acessor methods(getters), mutator methods(setters) ###################

#Accessor methods allow us access to the data inside an object. 
#these are frequently called 'getters', because these methods typically
#start with the word get.
import math

class Planet:
    #__init__ is the constructor.
    def __init__(self, name, radius, mass, distance):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.distance = distance
    #GETTERS
    def get_name(self): #all methods REQUIRE at least 'self' to be passed.
        return self.name 
        #self. gets us the planet name, because the 'name' variable
        # alone doesn't exist inside this tiny method,
        # we call it from the class.
    def get_radius(self):
        return self.radius
    def get_mass(self):
        return self.mass
    def get_distance(self):
        return self.distance
    
    def get_volume(self):
        volume = 4/3 * math.pi * self.radius ** 3
        return volume
    def get_density(self):
        density = self.mass / self.get_volume()
        #notice how we can use self on a separate method in order to
        #properly call the info from the "self" attributes in the class
        #which we define on our own.
        return density
    
    #SETTERS
    def set_name(self, new_name): #Setters need a new variable to be declared alongside self.
        self.name = new_name
        #notice how setters don't have a return value?
            #That's because it doesn't need to send any info back,
            #it just changes the current info.
    def set_radius(self, new_radius):
        self.radius = new_radius
    def set_mass(self, new_mass):
        self.mass = new_mass
    def set_distance(self, new_distance):
        self.distance = new_distance

    def __str__(self):
        message = ''
        message += f'hello {self.name}. how are you?'
        return message


planet1 = Planet('X25', 45, 198, 1000)
planet2 = Planet('Z37', 123, 454, 2320)

print(planet1.get_name())
print(planet2.get_name())
print(planet2.get_density())

print(planet1)
print(planet2)
#Mutator methods - are methods that mutate or change and object
#in someway. These are frequently called 'setters', as they set the
#value of some data, and frequently start with the word 'set'

#There's a special method in python called __str__() which is what
#the print function prints. By default, __str__() is class name and
#location in memory. We can change this using a procedure called
#overriding.









































