#Created by Bjorn Eriksson

#Question 1: Heads or Tails

def toss_coin(guess = 0):
    guess = input("Guess if the coin will be heads or tails: ")
    #0 is heads, 1 is tails
    from random import randint
    value = randint(0,1) #picks a random integer. Either 0 or 1
    if guess == 'heads':
        guess = 0
    elif guess == 'tails':
        guess = 1
    elif guess != 'heads' or guess != 'tails':
        guess = 0
    if guess == value:
        print("Correct!")
    elif guess != value:
        print("Incorrect!")
#toss_coin( )
#toss_coin(0)
#toss_coin(1)

#Question 2

def odd_or_even(guess = 'even'):
    from random import randint
    value = randint(0,9) #picks a random integer between 0-9 inclusive
    guess = input("Guess if the random value is odd or even: ")
    if value % 2 == 0:
        value = "even"
    elif value % 2 != 0:
        value = "odd"
    #if guess != 'even' or guess != 'odd':
        #guess = 'even'
    if guess == value:
        print("Correct!")
    elif guess != value:
        print("Incorrect!")
#odd_or_even()
#odd_or_even("odd")
#odd_or_even("even")

#Question 3: Copies of the same nuber

def count_duplicates(num1 = 0, num2 = 0, num3 = 0):
    if num1 == num2 == num3:
        return("There are 3 matches")
    elif num1 == num2 or num1 == num3 or num2 == num3:
        return("There are 2 mathces")
    else:
        return("All numbers are unique.")

print(count_duplicates(2, 3, 2))
print(count_duplicates(4, 4, 4,))
print(count_duplicates(1, 2, 3,))
print(count_duplicates(1))
print(count_duplicates(0))













#Question 7- incomplete
def ascending_order(num1, num2 = 5, num3 = 25): #num2 and 3 should be optional
    #if a > b swap
    if num1 > num2:
        return [num2, num1, num3]
    #if a > c swap
    if num1 > num3:
        return [num3, num1, num2]
    #if b > c swap
    if num2 > num3:
        return [num1, num2, num3]
#print(ascending_order(2, 3, 1))
#print(ascending_order(10, 1))
#print(ascending_order(50))












#Question 15 - Study how the different functions interact with each other

def is_negative(number):
    if number < 0:
        return True
    else:
        return False

def is_odd(number):
    return number % 2 != 0
       

def report_negative_odds(list_of_numbers):
    new_list = []
    for num in list_of_numbers:
        if is_negative(num) and is_odd(num):
            new_list.append(num)
    return new_list

#print(report_negative_odds([100,-57,12,1,-36,-15]))
#print(report_negative_odds([121,-101,36,-19,-6,0,21,-1]))
#print(report_negative_odds([-100,7,8437]))




















