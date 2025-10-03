#Created by Bjorn Eriksson

########### Day 1: I overslept. ############





########### Day 2: Dictionaries ############

#Write a function that takes a string and returns a list containing 
# all if the words that have at least two vowels

def string_to_list_with_vowels(word):
    words = []
    #collect a word
    built_word = ''
    vowel_count = 0
    for letter in word:
        if letter == ' ':
            if vowel_count >= 2:
                #add built_world into the list
                words.append(built_word)
            built_word = ''
            vowel_count = 0 #This is so the counter gets reset for each word
        else:
            built_word += letter
            if letter in 'aeiou':
                vowel_count += 1
    if vowel_count >= 2:
        words.append(built_word)
    return words

my_word = 'peter piper picked a peck of pickled peppers'
#print(string_to_list_with_vowels(my_word))


#how many times did I use each letter? ^

#  to initialize a dictionary, we use {}

phonebook = {'matt':5073891438, 'ashley':1234}
#print(phonebook)

#To add a key-value pair to a dictionary, we use
#dict_name[ key ] = value

phonebook['Waters'] = 6789
#print(phonebook)

#to look up a value in a dictionary, we use
#dict_name [ key ]. This will print the value

#print(phonebook['matt'])


for name in phonebook:
    print(f'{name} -> {phonebook[name]}')

#All we need to know about dictionaries ^
#Now, time for some better examples.


#how many times did I use each letter?

def letter_counter(word):
    #IDEA: make a dictionary where the letters are keys and the number of 
    # occurancies of the letter is the value.
    letter_dictionary = {}
    for letter in word:
        if letter in letter_dictionary:
            letter_dictionary[letter] = letter_dictionary[letter] + 1
        else:
            letter_dictionary[letter] = 1
    return letter_dictionary

#print(my_word)
#print(letter_counter(my_word))

#Instead of counting letters, try counting the amount of unique words instead.

def unique_word_count(data):
    lyst_data = data.split()
    word_dict = {}
    for word in lyst_data:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict

my_words = 'hello world programming swedish effectively introductionary obtuse'

x = unique_word_count(my_words)
for key in x:
    if len(key) >= 10: #Makes it so only big words get printed
        print(key, x[key])














































