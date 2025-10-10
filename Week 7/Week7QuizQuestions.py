#Created by Bjorn Eriksson
#Dictionaries 

#Example
#dict1 = {'01234' : 'Evan', '45678' : 'Jacob', '98765' : 'Matt'}

#for techid in dict1:
    #name = dict1[techid]
    #print(name)

#1: How to add a new record to a dictionary
# dict[12345] = 'Dave'
#2: How to increment
# dict['cow'] += 1
#3: How to iterate
# for key in dict:
#4: how to search in dictionaries
# if 'cow' in dict: / if 'cow' not in dict:



#Question 4

def get_names(name_dict):
    return list(name_dict.values())

#print(get_names({'01475' : 'Steve', '87469' : 'Alice', '654123' : 'Bob'}))
    

#Question 5

def find_oldest(age_dict):
    oldest_person = ''
    max_age = -1
    #Iterate through dict
    for curr_name in age_dict:
        #Extract the age of the current person
        curr_age = age_dict[curr_name]
        #Compare current persons age with max age
        if curr_age > max_age:
            #If current age is larger, update max age
            max_age = curr_age
            oldest_person = curr_age
    #Return the oldest age
    return oldest_person


#Question 6

def letter_count(word):
    dict = {}
    #Iterate through word
    for letter in word:
    #check if each letter is in the dictionary already
        if letter not in dict:
            dict[letter] = 1 #adds to dict
        else:
            dict[letter] += 1 #incrementing
    return dict
    #if not, add it as 1.
    #if it is, +1 increment
#print(letter_count("mississippi"))


#Question 9

receipt = {'Side Salad' : 6, 'Chicken parm' : 12, 'Cookie' : 3}
#Separates values from Key-Value pairs
receipt_values = receipt.values()
#Adds the values up with the sum built-in-method
total_sum = sum(receipt_values)

print(total_sum)





























































