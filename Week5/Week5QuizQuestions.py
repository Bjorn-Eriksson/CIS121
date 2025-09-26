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

#Question 1S (Strings)
'''
def is_fever(temp):
    numTemp = temp[:-1]
    float(numTemp)
    #if temp[2] == 'F':
        #if numTemp >= 98.7:
'''

