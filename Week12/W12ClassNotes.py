#Created by Bjorn Eriksson

#Missed day 1: I/O files

################ Day 2:   #######################

#missing the numbers.txt file from day 1 for this code to 100% work
# serves primarily as an example
'''
from random import randint

new_file = open('numbers.txt','w')

for index in range(0,100):
    number = randint(50,250)
    new_file.write(f'{number}\n')

new_file.close()

my_file = open('numbers.txt','r')

data = my_file.readlines()

total = 0
count = 0

for number in data:
    total += int(number)
    count += 1

print(f'total = {total}')
print(f'avg = {total/count}')
'''
#New exmaple

new_file = open('family.txt', 'w') #The w means writing, r is reading

new_file.write('Name,age,occupation,hobby\n')
new_file.write('Matt,39,Teacher,Running\n')
new_file.write('Dexter,8,Student,Reading\n')
new_file.write('Ashley,38,Important Teacher,Learning\n')

new_file.close()


my_file = open('family.txt', 'r')#opens up file for reading

def starts_with_vowel(word): #Code for challenge problem below
    if word[0] in 'aeiouAEIOU':
        return True
    else:
        return False
    
total = 0 #Challenge problem 2
count = 0

data = my_file.readlines()
for line in data[1:]: #[1:] is string slicing, makes it so the first line (our format line) doesn't end up in the actual data
    line_data = line.split(",") #Separates strings via the entered value, called a delimitor
    name = line_data[0] #Genius way to separate data. Line 50 and 51 will be revolutionary for final retake.
    occupation = line_data[2]
    hobby = line_data[3]
    age = int(line_data[1])

    total += age #Challenge problem 2
    count +=1 

    if starts_with_vowel(occupation):
        print(f"{name} is an {occupation}, they're {age} years old.")
    else:
        print(f"{name} is a {occupation}, they're {age} years old.")

print(f'avg age = {total/count}') #Challenge problem 2

#Challenge problem: how do we make the code gramatically correct for Ashley's data?
#If a word starts with a vowel, make it an vs a
#Identify if occupation's first letter is a vowel

#Second challenge question: find the average age of the people provided in the code

#Add all the ages into a total and divide that total by the number of ages provided





















































