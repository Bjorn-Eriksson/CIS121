#Created by Bjorn Eriksson



################## Day 1: Loops and Iteration ########################

#Iteration practice with loops
'''
number = 1

while True:
    print(number)
    number += 1
'''


#print the numbers 1-10.
'''
number = 1

while number <= 10:
    print(number)
    number += 1
'''

#print all of the even numbers between 1-10.
#multiple ways to do this problem

#1st way
'''
number = 2
while number <= 10:
    print(number)
    number += 2
'''
#Alternate solution
#Can be switched to printing only odd number by switching the modulus (%) remainder from 0 to 1.
'''
number = 1
while number <= 10:
    if number % 2 == 0:
        print(number)
    number += 1
'''
#All of the loops above use a determinine amount of things, what if we had loops with an infinte possible amount of loops?
#print all of the odd numbers between 5 and some user given value. (inclusively, meaning including both end points)

#First posible solution
'''
start_num = 5
user_num = int(input("Enter a number: "))

while start_num <= user_num:
    if start_num % 2 == 1:
        print(start_num)
    start_num += 1
'''
#Find the sum of user entered values until the user types q (for quit)
'''
total = 0
#total at the start should be 0
user_input = input("Enter a number or type q to quit: ")

while user_input != 'q':
    total += int(user_input) #This changes the input from a string '' to an integer.
    user_input = input("Enter a number or type q to quit: ")

print(f'total = {total}')
'''

#'Flags' are common in more robust code: Here's code with a flag
'''
total = 0
user_input = ''
done = False #flag

while not done:
    user_input = input("Enter a number or type q to quit: ")
    if user_input != 'q':
        done = True
    else:
        total += int(user_input)

print(f"total = {total}")
'''

#print all of the numbers between 1-50 that are even but not divisible by 3.
#good example of using break & continue statements.
'''
number = 0
while number < 50:
    number += 1
    if number % 2 == 0:
        if number % 3 == 0: #if number is divisible by 3
            #I want to do nothing and go to the next number
            continue #will go back to the original condition without printing a false number/error
        print(number)
'''
########################### End of day 1 ################################

############################### Day 2: for loops ###################################

#Examples of for loops

#print all of the numbers 1-10 inclusively.
'''
for number in range(1,10+1): #the +1 ensures '10' is printed too.
    print(number)



#print all of the even numbers between 1-10
#First method
for number in range(1,11):
    if number % 2 == 0:
        print(number)
#second method
for number in range(2,11,2): #The third variable in range is the 'step size'. Increased from start up to the stop via the step size.
    print(number)
'''

#print all of the odd numbers between 5 and some user given value
'''
num = int(input("Enter a number: "))

for num in range(5,num+1):
    if num % 2 == 1:
        print(num)
'''


#find the sum of the user entered values until the user types q for done.
#BAD SOLUTION! Bound to only 50 variables because of (0,50) for the range.
'''
total = 0
for number in range(0,50):
    user_input = input("Enter a number: ")
    if user_input == 'q':
        break
    total += int(user_input)
print(f"total = {total}")
'''
#in certain situations, while loops are generally better than for loops.
'''
#Strings as a data type
print('a'+'b') #glues them together
print( 3 + 4 )#addition
print('3' + '4')#Glues them together
#print( 3 + '4') #value error!
'''
#COLLECTION DATA TYPES
'''
word = 'hello world'
print(word[1]) #this prints 'e', because of the string's indexed variables.
'''
#Slicing can be used to get subsequences of string data.
'''
print(word[2:8]) #-> llo wo

word = 'hello world'

for letter in word:
    print(letter)
'''
