#Created by Bjorn Eriksson

#Question 1

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    #Getters
    def get_name(self):
        return self.name
    def get_price(self):
        return self.price
    def get_quantity(self):
        return self.quantity

    #Setters
    def set_name(self, new_name):
        self.name = new_name
    def set_price(self, new_price):
        if new_price >= 0:
            self.price = new_price
    def set_quantity(self, new_quantity):
        if new_quantity >= 0:
            self.quantity = new_quantity
    
    def __str__(self):
        message = ''
        message += f"Product name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"
        return message
    
product1 = Product("Tomato", 4.99, 200)
#print(product1)

#Question 2
class Book:
    def __init__(self, title, author, page_count):
        self.title = title
        self.author = author
        self.page_count = page_count

    def get_title(self):
        return self.title
    def get_author(self):
        return self.author
    def get_page_count(self):
        return self.page_count
    
    def set_title(self, new_title):
        self.title = new_title
    def set_author(self, new_author):
        self.author = new_author
    def set_page_count(self, new_page_count):
        self.page_count = new_page_count
    
    def __str__(self):
        message = ''
        message += f"The book is {self.title}, written by {self.author}. It's page count is {self.page_count}"
        return message

book1 = Book("Hunger Games", "Bjorn", 400)
#print(book1)


#Question 3
class Movie:
    def __init__(self, title, director, runtime_minutes):
        self.title = title
        self.director = director
        self.runtime_minutes = runtime_minutes

    def get_title(self):
        return self.title
    def get_director(self):
        return self.director
    def get_runtime(self):
        return self.runtime_minutes
    
    def set_title(self, new_title):
        self.title = new_title
    def set_director(self, new_director):
        self.director = new_director
    def set_runtime(self, new_runtime):
        self.runtime_minutes = new_runtime

    def __str__(self):
        return f"The movie title is {self.title}, directed by {self.director}. It's {self.runtime_minutes} minutes long."
movie1 = Movie("Dune", "Denis Villenvuve", 250)
#print(movie1)
    
#Question 4
class Song:
    def __init__(self, title, artist, duration_seconds):
        self.title = title
        self.artist = artist
        self.duration_seconds = duration_seconds

    def get_title(self):
        return self.title
    def get_artist(self):
        return self.artist
    def get_duration_seconds(self):
        return self.duration_seconds
    
    def set_title(self, new_title):
        self.title = new_title
    def set_artist(self, new_artist):
        self.artist = new_artist
    def set_duration_seconds(self, new_duration_seconds):
        self.duration_seconds = new_duration_seconds
    
    def __str__(self):
        return f'Song name: {self.title}, Artist: {self.artist}, Duration: {self.duration_seconds} seconds.'

song1 = Song("505", "Arctic Monkeys", 304)
#print(song1)

#Question 5

class Employee:
    def __init__(self, name, title, salary):
        self.name = name
        self.title = title
        self.salary = salary
    
    def get_name(self):
        return self.name
    def get_title(self):
        return self.title
    def get_salary(self):
        return self.salary
    
    def set_name(self, new_name):
        self.name = new_name
    def set_title(self, new_title):
        self.title = new_title
    def set_salary(self, new_salary):
        if new_salary > 0:
            self.salary = new_salary

    def __str__(self):
        return f"I am {self.name}. I have a great job!"

    
    def greeting(self):
        return f"Hello. My name is {self.name}. I'm a {self.title}"
    
    def request_raise(self):
        new_amount = self.salary + (self.salary * 0.06)
        return f"I'm currently making {self.salary}. I'd like a new salary of {new_amount}"
'''
employee1 = Employee("Bjorn", "Programmer", 100)
print(employee1)
print(employee1.greeting())
print(employee1.request_raise())
'''

#Question 6

class Student:
    def __init__(self, name, major, GPA):
        self.name = name
        self.major = major
        self.GPA = GPA

    def get_name(self):
        return self.name
    def get_major(self):
        return self.major
    def get_GPA(self):
        return self.GPA
    
    def set_name(self, new_name):
        self.name = new_name
    def set_major(self, new_major):
        self.major = new_major
    def set_GPA(self, new_GPA):
        self.GPA = new_GPA
    
    def __str__(self):
        return f"Hello, I'm {self.name}, majoring in {self.major} with a GPA of {self.GPA}"


    def introduce(self):
        return (f"Hi. I'm {self.name}, I'm studying {self.major}.")
    
    def study_for_exam(self):
        oldGPA = self.GPA
        self.GPA += 0.2
        return (f"I'm hitting the books! My GPA increased from {oldGPA} to {self.GPA}")

'''
student1 = Student("Bjorn", "Comp Sci", 3.4)
print(student1)
print(student1.introduce())
print(student1.study_for_exam())
'''


#Question 7

class Vehicle:
    #Constructor method to initalize all instance variables
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    #getters
    def get_make(self):
        return self.make
    def get_model(self):
        return self.model
    def get_year(self):
        return self.year
    #setters
    def set_make(self,new_make):
        self.make = new_make
    def set_model(self, new_model):
        self.model = new_model
    def set_year(self, new_year):
        self.year = new_year

    def __str__(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}"

    def print_vehicle_type(self):
        return f"{self.year} {self.make} {self.model}"

'''
vehicle1 = Vehicle("Toyota", "Camry", "2021")
print(vehicle1)
print(vehicle1.print_vehicle_type())
'''

#Question 8
class Course:
    #Constructor method to initalize all instance variables
    def __init__(self, course_code, course_name, instructor):
        self.course_code = course_code
        self.course_name = course_name
        self.instructor = instructor

    #getters
    def get_course_code(self):
        return self.course_code
    def get_course_name(self):
        return self.course_name
    def get_instructor(self):
        return self.instructor
    #Setters
    def set_course_code(self, new_course_code):
        self.course_code = new_course_code
    def set_course_name(self, new_course_name):
        self.course_name = new_course_name
    def set_instructor(self, new_instructor):
        self.instructor = new_instructor
    
    def __str__(self):
        return f"Code: {self.course_code}, Name: {self.course_name}, Instructor: {self.instructor}"

    def print_info(self):
        return f"{self.course_code}: {self.course_name} taught by {self.instructor}"
'''
course1 = Course("CIS121", "Introduction to Programming", "Matt")
print(course1)
print(course1.print_info())
'''

#Question 9
class Point:
    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
    
    def get_x_coordinate(self):
        return self.x_coordinate
    def get_y_coordinate(self):
        return self.y_coordinate
    def set_x_coordinate(self, new_x):
        self.x_coordinate = new_x
    def set_y_coordinate(self, new_y):
        self.y_coordinate = new_y
    
    def __str__(self):
        return f"{self.x_coordinate}, {self.y_coordinate}"

    def print_info(self):
        return f"({self.x_coordinate},{self.y_coordinate})"
'''
point1 = Point(1,4)
print(point1)
print(point1.print_info())
'''

#Quesiton 10
import math
class Vector:
    def __init__(self, x_direction, y_direction):
        self.x_direction = x_direction
        self.y_direction = y_direction
    
    def get_x(self):
        return self.x_direction
    def get_y(self):
        return self.y_direction
    def set_x(self, new_x):
        self.x_direction = new_x
    def set_y(self, new_y):
        self.y_direction = new_y
    
    def __str__(self):
        return f"{self.x_direction}, {self.y_direction}"
    def get_magnitude(self):
        magnitude = math.sqrt((self.x_direction ** 2) + (self.y_direction ** 2))
        return magnitude
'''
vector1 = Vector(2,2)
print(vector1)
print(vector1.get_magnitude())
'''
#Question 11
class ColorRGB:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue=blue

    def get_red(self):
        return self.red
    def get_green(self):
        return self.green
    def get_blue(self):
        return self.blue
    def set_red(self, new_red):
        self.red = new_red
    def set_green(self, new_green):
        self.green = new_green
    def set_blue(self, new_blue):
        self.blue = new_blue
    
    def __str__(self):
        return f"red: {self.red}, green: {self.green}, blue: {self.blue}"
    
    def to_grayscale(self):
        value = (0.3 * self.red) + (0.59 * self.green) + (0.11 * self.blue)
        return value
'''
color1= ColorRGB(120,155,130)
print(color1)
print(color1.to_grayscale())
'''

#Question 12
class TempInC:
    def __init__(self, temp_value):
        self.temp_value = temp_value

    def get_temp_value(self):
        return self.temp_value
    def set_temp_value(self, new_val):
        self.temp_value = new_val
    
    def __str__(self):
        return f"Temp value: {self.temp_value} C"
    
    def to_farenheight(self):
        farenheight = (self.temp_value * (9/5) + 32)
        return farenheight
'''
temp1 = TempInC(20)
print(temp1)
print(temp1.to_farenheight())
'''

#Question 13
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def get_width(self):
        return self.width
    def get_height(self):
        return self.height
    def set_width(self, new_width):
        self.width = new_width
    def set_height(self, new_height):
        self.height = new_height
    
    def __str__(self):
        return f"Width: {self.width}, Height: {self.height}"
    
    def calculate_area(self):
        area = self.width * self.height
        return area
'''
rectangle1 = Rectangle(2,4)
print(rectangle1)
print(rectangle1.calculate_area())
'''










#Question 15
class Recipe:
    def __init__(self, name, cooking_time):
        self.name = name
        self.cooking_time = cooking_time #Consider the time in mins.
    
    def get_name(self):
        return self.name
    def get_cooking_time(self):
        return self.cooking_time
    def set_name(self, new_name):
        self.name = new_name
    def set_cooking_time(self, new_cooking_time):
        self.cooking_time = new_cooking_time
    
    def __str__(self):
        return f"{self.name}, {self.cooking_time} to cook."

    def is_quick_meal(self):
        if self.cooking_time < 30:
            return True
        elif self.cooking_time >= 30:
            return False
'''
recipe1 = Recipe("Chicken", 20)
recipe2 = Recipe("Stew", 50)

print(recipe1)
print(recipe2)

print(recipe1.is_quick_meal())
print(recipe2.is_quick_meal())
'''














































