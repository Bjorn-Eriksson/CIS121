#Created by Bjorn Eriksson

#Question 1F (Functions)
import math

'''
def pyramid_volume(base, height):
    volume = ((base ** 2) * height) / 3
    return(volume)

print(pyramid_volume(1, 2))
print(pyramid_volume(2, 2))
print(pyramid_volume(3, 4))
'''

#Question 2F
'''
def cone_volume(radius, height):
    volume = (math.pi * ((radius ** 2) * height) / 3)
    return volume

print(cone_volume(1, 2))
'''

#Question 3F













#Question 8F (Functions)
'''
def pool_hours(input_grade, input_time):
    pool_hours = ''
    if input_grade == 'k':
        input_grade = 0

    if input_grade <= 0 and input_grade >= 3:
        if input_time == 'Morning':
            pool_hours = '9 AM'
        elif input_time == 'Afternoon':
            pool_hours = '1 PM'
    elif input_grade <= 4 and input_grade >= 8:
        if input_time == 'Morning':
            pool_hours = '10 AM'
        elif input_time == 'Afternoon':
            pool_hours = '2 PM'
    #elif input_grade <= 9 and input_grade >= 12:
        #Finish the rest later
'''


#Question 11F (Functions)
'''
def convert_knuts(knuts):
    output = ''
    
    galleons = knuts // 493 # or (29 * 17) 
#First, we separate into the highest currency. // makes no remainder.
    remaining_knuts = knuts % 493
#Then, we take the remaining knuts and ensure we can't make a new galleon.
    sickles = remaining_knuts // 29
#Taking the now sorted Knuts, we see how many Sickles we can get from it.
    remaining_knuts = remaining_knuts % 29
#Doing the // and %, we can separate the sickles into a sorted variable
# then, by doing the modulous we get the remaining amount of knuts from
# the sickle separation.
    if galleons > 0:
        output += (f'Galleons: {galleons} ')
    if sickles > 0:
        output += (f'Sickles: {sickles} ')
    if remaining_knuts > 0:
        output += (f'Knuts: {remaining_knuts} ')
#These if statements are incase there's 0 knuts, it won't print a value of 0.
#doing 'output += .....' allows us to pick and choose what we print.
    return output

input_knuts = int(input("Enter the amount of Knuts: "))
print(f'{convert_knuts(input_knuts)}')
'''
#Logic behind question 11F;

# 29 * 17 = 493

#544 knuts, how many galleons can i buy? 
# 1, because 544/493 = 1

#After buying 1 galleon, how many knuts remain?
# 544 % 493 = 51

#51 Knuts, how many sickles can i buy?
# 51 // 29 = 1

#Remaining knuts = 51 - (29 * 1) = 22


#Question 14F, Odd or Even
'''
from random import randint
value = randint(0,9) #picks a random integer between 0-9 inclusive.

def guess_num(guess):
    if value % 2 == 0:
        if guess == 'even':
            print("Correct!")
        if guess == 'odd':
            print("Incorrect.")
    elif value % 2 == 1:
        if guess == 'even':
            print("Incorrect.")
        if guess == 'odd':
            print("Correct!")
guess_num('odd')
'''


########################################### STRINGS! ###########################################

#Question 1 S (Strings)


#Question 2 S 
'''
def is_fever(input_temp):
    output = False

    #Issue 1: how can we excract the temp to determine if F/C
    unit = input_temp[-1]

    #Issue 2: how can we extract the temperature?
    temp = int(input_temp[:-1])

    #Issue 3: If F, > 98.6 = Fever
    if unit == 'F' and temp > 98.6:
        output = True
    #Issue 4: If C, > 37.0 = Fever
    if unit == 'C' and temp > 37:
        output = True

    return output
user_input = input("Enter a temp 00F, 00C: ")
print(f'This temp {user_input} is fever? {is_fever(user_input)}')
'''
#Question 3 S

def is_boiling(temp):
    unit = temp[-1]
    value = int(temp[:-1])

    if unit == 'F' and value >= 212:
        print("True")
    elif unit == 'F' and value < 212:
        print("False")
    if unit == 'C' and value >= 100:
        print("True")
    elif unit == 'C' and value < 99:
        print("False")
is_boiling("212F")
is_boiling("100C")
is_boiling("0F")










#Question 4 S
'''
def hamming_distance(str1, str2):
    counter = 0
    if len(str1) != len(str2):
        return 0
        #Make this first if statement more efficient, printing a diff outcome if the words
        # aren't the same length.
        
    for i in range(0, len(str1)):
        if str1[i] != str2[i]:
            counter += 1

    return counter
word1 = input("Enter a word: ")
word2 = input("Enter a word(Match character # from previous word): ")

print(f'The hamming distance between {word1} and {word2} is {hamming_distance(word1, word2)}')
'''





#Question 8 S 
'''
def last_letters(sentence):
    encode = ''
    #1. How to iterate through the characters
    for pos in range(0, len(sentence) -1):


    #2. How can we know the last letter of each word?
    # 'wingardium levios makes objects float '

        if sentence[pos + 1] == ' ':
            encode += sentence[pos]

    #3. How do we store the last characters and output it?
    return encode + sentence[-1]
user_input = input("Enter a spell: ")
print(f'Encoded Spell is {last_letters(user_input)}')
'''

#Question 9 S Unfinished
'''
def flip_flop(word):
    length = len(word)
    midpoint = length // 2
    
    first_half = word[:midpoint]
    second_half = word[midpoint]
    return second_half + first_half
print(flip_flop('cranberries'))
'''



















