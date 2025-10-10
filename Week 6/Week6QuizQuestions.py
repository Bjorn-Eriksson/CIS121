#Created by Bjorn Eriksson



#Question 1: incomplete

def skip_letter(word):
    new_word = []
    for letter in range(0, len(word) +1, 2):
        #if letter == ' ':
            #continue
        if letter != ' ':
            new_word.append(word[letter])
        
    print(new_word)

#skip_letter('counterattack') # c u t r t a k
#skip_letter('banana sunday') #b n n s n a


#Question 2

def skip_letter(word):
    new_word = []
    for letter in range(1, len(word) +1, 2):
        #if letter == ' ':
            #continue
        if letter != ' ':
            new_word.append(word[letter])
        
    print(new_word)

#skip_letter('counterattack') # c u t r t a k
#skip_letter('banana sunday') #b n n s n a


#Question 3

def output_even(smaller_num, larger_num):
    even_numbers = []
    
    #If smaller number is odd, add 1 to start from the next even number.
    if smaller_num % 2 != 0:
        smaller_num += 1
    for number in range(smaller_num, larger_num + 1, 2):
        even_numbers.append(number)
    
    return even_numbers
#print(output_even(37, 1050))
#print(output_even(1, 2000))
#print(output_even(50, 199))


#Question 4

def output_odd(smaller_num, larger_num):
    odd_numbers = []
    
    #If smaller number is even, add 1 to start from the next even number.
    if smaller_num % 2 != 1:
        smaller_num += 1
    for number in range(smaller_num, larger_num + 1, 2):
        odd_numbers.append(number)
    
    return odd_numbers
#print(output_odd(37, 1050))




#Question 5

def hailstone_seq(num):
    hailstone_list = []

    while num != 1:
        #While the number isn't 1, add it to the list
        hailstone_list.append(int(num))
        #From there, if it's even we divide number by 2
        if num % 2 == 0:
            num = num /2
        #If it's odd, we mult by 3 and add 1.
        else:
            num = (num * 3) + 1
    hailstone_list.append(1)
    #This ensures that there's a 1 at the end of the list, because the
    #Loop stops at 1.
    return hailstone_list
    

#print(hailstone_seq(25))
#print(hailstone_seq(40))

#Question 6

def find_factors(num):
    factors = []
    for i in range(1, num + 1):
        #Check if 'i' divides number evenly
        if num % i == 0:
            #Add it to the list
            factors.append(i)
    return factors
#print(find_factors(36))

#Question 7

def ascending_order(num_1, num_2, num_3):
    #Case 1: num1 is smallest
    if num_1 <= num_2 and num_1 <= num_3:
        #If 1 is smaller than 2 & 3:
        if num_2 <= num_3:
            #If 2 is smaller than 3:
            return [num_1, num_2, num_3]
            #print 1 2 3
        else:
            return [num_1, num_3, num_2]
            #print 1 3 2
    
    #Case 2: num2 is smallest
    elif num_2 <= num_1 and num_2 <= num_3:
        #If 2 is smaller than 1 & 3
        if num_1 <= num_3:
            #If 1 is smaller than 3
            return [num_2, num_1, num_3]
            #print 2 1 3
        else:
            return [num_2, num_3, num_1]
            #print 2 3 1
    
    #Case 3: num3 is smallest
    else:
        if num_1 <= num_2:
            return [num_3, num_1, num_2]
            #print 3 1 2
        else:
            return [num_3, num_2, num_1]
            #print 3 2 1
#At it's core, this code is asking for the first smallest, then the second
#smallest, and printing the resulting pattern.







#Question 9 

def count_cards(card_list):
    if len(card_list) == 0:
        return "Error"
    total = 0
    list1 = [2, 3, 4, 5, 6]
    list2 = [7, 8, 9]
    list3 = [10, 'j', 'q', 'k', 'a']
    
    for card in card_list:
        if card in list1:
            total += 1
        elif card in list2:
            total += 0
        elif card in list3:
            total -= 1
    return total

#print(count_cards[5, 9, 10, 3, 'j', 'a', 4, 8, 5])

#Question 10

def war_of_numbers(numbers):
    even_sum = 0
    odd_sum = 0

    for number in numbers:
        if number % 2 == 0:
            even_sum += number
        else:
            odd_sum += number

    if even_sum > odd_sum:
        return "even"
    elif odd_sum > even_sum:
        return "odd"
    else:
        return "tie"
#print(war_of_numbers([2, 8, 7, 5]))

#Question 12 (Error shows up still)

def largest_even(numbers):
    largest_even = -1
    found_even = False

    for num in numbers:
        if num % 2 == 0:
            if not found_even:
                largest_even = num
                found_even = True
            elif num > largest_even:
                largest_even = num
    if not found_even:
        return '-1'
    else:
        return largest_even
#print(largest_even[3, 7, 2, 1, 7, 9, 10, 13])

#Question 14

def progress_days(miles):
    progress = 0
    for day in miles:
        if day > miles:
            progress += 1
    return progress
print(progress_days[3, 4, 1, 2])



#Question 19

def is_acronym(string, list_of_words):
    
    #Compare length
    if len(string) != len(list_of_words):
        return False
    
    first_letters = ''

    #Iterate through each word
    for word in list_of_words:
        #For each word...
        #Check if a word is empty
        if word == '':
            return False
        #If not empty, get letter of each word
        #Get first letter of each word
        first_letter = word[0]

        #Add each first letter to a variable 
        first_letters += first_letter

    #Compare
    if first_letters != string:
        return False

    return True

#is_acronym('abc', ['Alice', 'bob', 'charlie'])

# OR you can do Q 9 like this: (unfinished)

'''
if len(string) != len(list_of_words):
    return False

for i in range(0, len(list_of_words)):
    if string[i] != list_of_words[i][0]

return True
'''


























