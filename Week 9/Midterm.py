#Created by Bjorn Eriksson
#Missed standards:
#7.3, Use iteration to traverse a list, extract and aggregate data,
#  and apply the results to a subsequent computational task or analysis.

#8.1, Initialize and load a directory

#8.2, Utilize iteration to traverse a dictionary and identify a
# specified value or criteria.


#7.3: Lists
#Question 14

def progress_days(miles):
    progress = 0
    for i in range(1, len(miles)): #for loop to run through a list
        if miles[i] > miles[i - 1]: #if current num in list is greater than the previous number
            progress += 1 #adds a progress day
    return progress
'''
print(progress_days([3, 4, 1, 2,]))
print(progress_days([10,11,12,9,10]))
print(progress_days([6,5,4,3,2,9]))
print(progress_days([9,9]))
'''    

#8.1 & 8.2: dictionaries

#Question 1

def is_isogram(word):
    dict = {}
    for letter in word:
        if letter not in dict:
            dict[letter] = 1 #Adds letter to dict
        elif letter in dict:
            dict[letter] += 1

    if dict[letter] > 1:
        print("False")
    elif dict[letter] <= 1:
        print("True")
'''
is_isogram('algorism')
is_isogram('password')
is_isogram('consecutive')
'''

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

#print(find_oldest({'Emma':71,'Jack':45,'Olivia':82,"Liam":39}))

#Question 4









#Question 13

def total_sales(sales):
    for i in sales:
        total  = sum(sales.values())
    return total

#print(total_sales({'Laptop' : 5, 'Phone' : 10, 'Tablet' : 3}))








































