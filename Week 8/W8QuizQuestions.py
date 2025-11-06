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
'''
print(count_duplicates(2, 3, 2))
print(count_duplicates(4, 4, 4,))
print(count_duplicates(1, 2, 3,))
print(count_duplicates(1))
print(count_duplicates(0))
'''
#Question 4:

def rock_paper_scissors(player1 = 'Rock', player2 = 'Rock'):
    if player1 == player2: #Covers any tie, more efficient than doing 3 diff ties.
        return "It's a tie!"
    elif player1 == 'Rock' and player2 == 'Scissors': #The next 3 elif
        return "Player 1 wins!"            #Statements cover all of P1's
    elif player1 == 'Scissors' and player2 == 'Paper': #wins, then
        return 'Player 1 wins!'            #we just do an else to cover
    elif player1 == 'Paper' and player2 == 'Rock': #player 2.
        return 'Player 1 wins!'
    else:
        return "Player 2 wins!"
'''
print(rock_paper_scissors('Rock', 'Paper'))
print(rock_paper_scissors('Scissors', 'Paper'))
print(rock_paper_scissors('Rock', 'Rock'))
print(rock_paper_scissors('Rock'))
print(rock_paper_scissors())
print(rock_paper_scissors('Scissors'))
'''

#Question 5:
def find_relation(name = ''):
    if name == 'Darth Vader':
        return "Father"
    elif name == 'Leia':
        return "Sister"
    elif name == 'Han':
        return 'Brother in law'
    elif name == 'R2D2':
        return 'Droid'
    else:
        return 'Unknown'
'''
print(find_relation("Darth Vader"))
print(find_relation("R2D2"))
print(find_relation("Jabba the Hutt"))
print(find_relation())
'''

#Question 6

def hailstone_seq(n = 40):
    print(n, end=' ') #This prints the starting number, end=' ' prevents the code from going to a newline.
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        print(n, end=' ') #prints n after all the math goes through
    print() #Without this, it would put 'none' at the end of the sequence.
'''
print(hailstone_seq(25))
print(hailstone_seq(40))
print(hailstone_seq())
'''


#Question 7- incomplete
def ascending_order(num1, num2 = 5, num3 = 25): #num2 and 3 should be optional
    numbers = [num1, num2, num3]
    #Compare and swap the first and second numbers
    if numbers[0] > numbers[1]: 
        numbers[0], numbers[1] = numbers[1], numbers[0]
    #Compare and swap the second and third numbers
    if numbers[1] > numbers[2]: 
        numbers[1], numbers[2] = numbers[2], numbers[1]
    #Re-compare first and second numbers incase third number 
    #pushed a larger number to the second position.
    if numbers[0] > numbers[1]: 
        numbers[0], numbers[1] = numbers[1], numbers[0]
    return numbers
    #Order of operations:
    #If 0 > 1: [1,0,2]
    #If 1 > 2: [1,2,0]
    #If 0 > 1: [2,1,0]
    
print(ascending_order(2, 3, 1))
print(ascending_order(10, 1))
print(ascending_order(50))







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




















