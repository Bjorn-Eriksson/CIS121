#Created by Bjorn Eriksson

#Question 1:
'''
num1 = float(input("Enter a number: "))
num2 = float(input("Enter a second number: "))
counter = 0

while num1 > num2:
    num1 /=2 
    counter += 1
print(counter-1)
'''
#Question 2:
'''
user_word = input("Enter a word: ")

for index in range(1, len(user_word) [2]):

#Safer way to write this;
for index in range(len(user_word)):
    if index % 2 == 1:
        print(#something)
'''
#Question 3, print every even number between 37 and 1050 (Inclusively)
#num1 = 1050
#num2 = 37
'''
for number in range(38, 1051, 2):
    print(number)
'''

#Question 4
'''
word = ''

while True:
    letter = input("Enter a letter (or type done): ")
    if letter == 'done':
        break
    word += letter

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

total = 0
#user_input = int(input("Enter a number: "))

while True:
    user_input = int(input("Enter a number: "))
    



































