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


    
    



















































































