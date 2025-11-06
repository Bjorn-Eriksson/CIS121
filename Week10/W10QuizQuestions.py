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


    def introduce(self, student_name, student_major):
        for name in self.name:
            if student_name == name and student_major == self.major:
                print(f"Hi. I'm {student_name}, I'm studying {student_major}.")
    
    def study_for_exam(self):
        #INCOMPLETE


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

    def print_vehicle_type


















































