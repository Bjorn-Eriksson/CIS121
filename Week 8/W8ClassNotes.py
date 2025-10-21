#Created by Bjorn Eriksson

############# Day 1:  ###############
#Learning about python debugger mode

#Store a list of words consisting of all words with 2 or more vowels.
#Click on left of the line counter to add a red dot, that's the stopping point for the debugger
def string_to_list_with_vowels(word):
    words = []
    #Collect a word
    built_word = ''
    vowel_count = 0
    for letter in word:
        if letter == ' ':
            words.append(built_word)
            built_word = ''
        else:
            built_word += letter
    return words
    
my_word = 'peter piper picked a peck of pickled peppers'
print(string_to_list_with_vowels(my_word))

################## Day 2:   ##########################











































































