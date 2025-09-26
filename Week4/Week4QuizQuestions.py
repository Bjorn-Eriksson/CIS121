#Created by Bjorn Eriksson

#Question 1:
'''
num1 = float(input("Enter a number: "))
num2 = float(input("Enter a second number: "))
counter = 0

while num1 > num2:
    num1 /= 2 
    counter += 1
print(counter-1)
'''
#Question 2:
'''
user_word = input("Enter a word: ")
for letter in range(1, len(user_word)): #This makes it so the loop runs for the length of the word
    if letter % 2 == 1: #Modulous of 1 means it's skipping the 'even' indexes 
        print(user_word[letter]) #This prints the word's Modulous'd index. Essentially skipping all the evens
'''

#Question 3, print every even number between 37 and 1050 (Inclusively)
#num1 = 1050
#num2 = 37
'''
for number in range(38, 1051, 2): #If we started the range at 37, it would increase by 2, printing odd.
    print(number)
#1051 for the range is because range doesn't include the final number, only upto it.
'''
#Question 4
'''
word = ''

while True: #Means we can choose when it's false at any time with a break statement.
    letter = input("Enter a letter (or type done): ")
    if letter == 'done':
        break
    word += letter #This just smushes the letter we type onto the empty string outside the loop.
    #The reason it's after the break statement is that it would print 'done' at the end of our word 
    #if we had it after the string concadonation bit.
print(word)
'''
#Question 5: Loop to calculate sum of all odd number between 50 and 517. Print result
'''
sum = 0

for num in range(51, 518, 2):
    sum += num
print(sum)
'''
#Question 6: Repeatedly ask user for integers until negative int is given. Print the sum at the end 
#NOT including the negative number
'''
total = 0

while True:
    user_num = int(input("Enter a number: "))
    if user_num < 0:
        break
    total += user_num

print(total)
'''

#Question 7, write a hailstone sequence starting at n = 25
  #if n is even, divide by 2
  #if n is odd, multiply by 3 and add 1 (3n + 1)
  #continue until n is 1.
'''
number = 25

while number != 1: #Hailstone sequence stops at 1, so we have our loop run till it hits 1.
    if number % 2 == 0: #if even
        number = number / 2
    else: #if odd
        number = (number * 3) + 1
    print(number)
'''
#Question 8, code that asks the user for an integer, then prints each number that is
# a factor of the input
#ex: 12 -> 1 2 3 4 5 12
#Factor definition: whole numbers that can divide into the given number exactly, no remainder
'''
integer = int(input("Enter a number: "))

for num in range(1, integer +1): #So the loop runs the duration of our user given number.
    if integer % num == 0: #This will divide the user num by the entire range, starting from 1.
        print(num) #prints the num with no remainder, which are factors.
'''

#Question 9, program that asks for a width, length, and pattern. Then creating a box with
#The chosen pattern.
'''
width = int(input("Enter a width: "))
length = int(input("Enter a length: "))
pattern = input("Enter a pattern: ")

for i in range(0, length): #This means the loop will continue down however many times the length is set.
    for n in range(width):
        print(pattern, end='') #The end='' is so it doesn't print into a newline.
        #That way, it will properly print the width.
    
    print() #Makes a new line?
'''

#Question 10, Ask user for integers till a negative is given. Report back the largest
# EVEN number the user entered (Not including the negative number)
'''
bignum = 0

while True:
    user_num = int(input("Enter a number: "))
    if user_num < 0: #Allows the loop to continue so long as we don't enter a negative.
        break
    elif user_num >= bignum and user_num % 2 == 0: #if new num is greater than old and EVEN
        bignum = user_num
    elif user_num >= bignum and user_num % 2 == 1: #if new num is odd
        bignum = -1
print(f'largest = {bignum}')
'''

#Question 11, Write code that asks user for an int, Calculate (and print) the sum of 
# all square numbers up to and including the users number.
'''
sum = 0
user_num = int(input("Enter a number: "))

for num in range(0, user_num+1):
    num **= 2 #Makes it so the number gets squared first
    sum += num #Then added to the total.
print(sum)
'''

#New Questions professor forgot to include

#Build a pyramid with a user-defined height out of asterisks '*'

height = int(input("Enter a height: "))
symbol = '*'

for block in range(0, height):
    print(symbol)
    symbol += '*'
































