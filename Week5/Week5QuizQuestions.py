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

#Question 8F (Functions)

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



#Question 11F (Functions)
'''
def convert_knuts(knuts):
    output = ''
    
    galleons = knuts // 493 # or (29 * 17)

    remaining_knuts = knuts % 493

    sickles = remaining_knuts // 29

    remaining_knuts = remaining_knuts % 29

    if galleons > 0:
        output += (f'Galleons: {galleons} ')
    if sickles > 0:
        output += (f'Sickles: {sickles} ')
    if remaining_knuts > 0:
        output += (f'Knuts: {remaining_knuts} ')

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














