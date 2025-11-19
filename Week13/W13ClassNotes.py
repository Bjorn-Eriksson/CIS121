#Created by Bjorn Eriksson

################# Day 1: We're ahead of scheule, so this week will be devoted to Exceptions  ####################

#Any project submitted before the 25th will be graded and be given another chance for revision before the hard deadline
#For submission, exactly 1 person per group should submit and have all the names on it.
# also, submit a word doc/readme file alongside it briefly decribing where we wan't matt to read. (Only matters if its hundreds of lines of code)
#      ex: "Here are 3 functions on line 3,7,12. Function x is called on lines blah, blah, blah"


################# Class code: #############
'''
print("Hello world")

user_input = input("What is your age?: ")
user_age = int(user_input)

print(f'Your age is {user_age}')
print(f'Your age next year is {user_age + 1}')
'''
'''
print('start')
try:
    print(x)
    #block of code
    #this will attempt the code in this block and if an error occurs
    #it will send that error to the EXCEPT blocks

except ValueError:
    print("You have a value error")
except TypeError:
    print("You have a type error")
except NameError:
    print("You have a name error")

print('end')
'''

print('start')
print("Enter a number. I will divide 10 by that number, an output the result")

done = False
while not done:

    try:
        user_input = input("pick a number: ")
        user_number = int(user_input)
        result = 10/user_number
        print(f'result = {result}')
        done = True

    except ValueError:
        print("Don't pick a letter")
    except ZeroDivisionError:
        print("You can't divide by 0")

print('end')








































