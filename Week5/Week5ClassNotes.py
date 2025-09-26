#Created by Bjorn Eriksson

############### Day 1, strings, len, def, & return inside functions. #################

#Write code to determine how many letters are in a word.
'''
word = 'hello world'

count = 0

for letter in word:
    count += 1
print(count)

print('\n-----------\n')
#Alternate solution, the len operator
#len - reports the length of an object (the word).
for index in range(0,len(word)): #range goes 0-11 for 'hello world', but doesn't count the end (which is good for this example)
    print(index, word[index])
'''
#Write code to determine how many vowels are in a word "AEIOU"
'''
word1 = input("Enter your first word(lowercase): ")
word2 = input("Enter your second word(lowercase): ")
word3 = input("Enter your third word(lowercase): ")
count1 = 0
count2 = 0
count3 = 0

for letter in word1:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        count1 +=1
for letter in word2:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        count2 +=1
for letter in word3:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        count3 +=1

print(f'The vowel count in {word1} is {count1}.')
print(f'The vowel count in {word2} is {count2}.')
print(f'The vowel count in {word3} is {count3}.')
'''
#While the above is expandable exponentially, it's a pain to write/paste all that code.
#We need some way to hold all of this code.

#We can make our OWN functions with def
'''
def vowel_counter(word):
    count = 0
    for letter in word:
        if letter == 'a':
            count += 1
        elif letter == 'e':
            count += 1
        elif letter == 'i':
            count += 1
        elif letter == 'o':
            count += 1
        elif letter == 'u':
            count += 1
    print(f"The vowel count in {word} is {count}")
#Now that we defined the vowel counter function, all we need to do is call the function like we call a print statement

#return gives back information from a function

vowel_counter('hello world')
vowel_counter('apples and bananas')
vowel_counter('happy times')

#Write a function that returns the number of vowels in a word using our previous function.

def vowel_counter_with_return(word):
    count = 0
    for letter in word:
        if letter == 'a':
            count += 1
        elif letter == 'e':
            count += 1
        elif letter == 'i':
            count += 1
        elif letter == 'o':
            count += 1
        elif letter == 'u':
            count += 1
    #NEW STUFF, return function
    return count
word1 = 'hello world'
word2 = 'apples and bananas'
word3 = 'happy times'

vowel1_count1 = vowel_counter_with_return(word1)
vowel1_count2 = vowel_counter_with_return(word2) #This is simply storing the information, not printing.
vowel1_count3 = vowel_counter_with_return(word3)

total_vowel_count = vowel1_count1 + vowel1_count2 + vowel1_count3

print(f'the total vowels seen so far is {total_vowel_count}')
'''
################## Day 2, #####################

#Write a function that takes an int & adds two, multiplies by 4, then returns result.

def add2mult4(number):
    number += 2
    number *= 4
    return number

result1 = add2mult4(10)
result2 = add2mult4(result1)
#print(result2)



#Testing
def add_5(number):
    number += 5
    return number

def times_2(number):
    number *= 2
    return number

x = times_2(add_5(10))
#is x == 30 or x == 25?
#It will == 30.


#Write a power of 2 function to calbulate ((3^2)^2)

def power_2(number):
    number **= 2
    return number

y = power_2(power_2(3))
#print(y)

#Using the times 2 function, multiply 5 by 2 a total of 10 times.
#We can use a loop.

result = 5
for value in range(0,10):
    result = times_2(result)
#print(result)

#write a function that returns the product of two arguments.

def product(num1, num2):
    result = num1 * num2
    return result

x = product(3, 2)
#print(x)

#Moving on from functions
#                          ------------------ LISTS! ------------------ #
#In Python, a list starts and ends with []
# x = [] is a list with nothing in it.

lyst = ['apple', 'banana', 3, False, 4.5, 'grapes']

#Write the code that prints the word banana from the list.

#print(lyst[1])

#Write code that prints 3, False, and 4.5

#print(lyst[2:5])

#Print the 'p' in 'grapes'

#print(lyst[5][3])

#Print every element of the lyst one at a time.
'''
for element in lyst: #Using range, it just iterates across the list.
    print(element)
'''
#lyst.append( element ) will add the element to the end of the list.
'''
print(lyst)
lyst.append(12)
print(lyst)
'''

#.insert can be used to put an element in the middle of a list









































































