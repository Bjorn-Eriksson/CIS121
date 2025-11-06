#Created by Bjorn Eriksson

#Qestion 1 :Debugger_p1_HarryPotter - Incomplete

def convert_knuts(knuts=900): #Error 1: Default should be 900 Knuts, not 450
	KNUTS_PER_SICKLE = 29
	SICKLES_PER_GALLEON = 17
	KNUTS_PER_GALLEON = KNUTS_PER_SICKLE * SICKLES_PER_GALLEON
				
	galleons = knuts // KNUTS_PER_GALLEON
	remaining_knuts = knuts // KNUTS_PER_GALLEON
				
	sickles = remaining_knuts // KNUTS_PER_SICKLE
	remaining_knuts = remaining_knuts // KNUTS_PER_SICKLE #Error 2, swapped from mod % to remainder //
	
	output = ""
	
	if galleons > 0:
		if galleons > 1:
			output = output + str(galleons) + " galleons"
		else:
			output = output + str(galleons) + " galleon"
	
	if sickles > 0:
		if output:
			output = output + " "
		if sickles > 1:
			output = output + str(sickles) + " sickles"
		else:
			output = output + str(sickles) + " sickle"
	
	if remaining_knuts > 0:
		if output:
			output = output + " "
		if remaining_knuts > 1:
			output = output + str(remaining_knuts) + " knuts"
		else:
			output = output + str(remaining_knuts) + " knut"
	
	return output
'''
print(convert_knuts(32)) #Expected: 1 sickle, 3 knuts
print(convert_knuts()) #Expected: 1 galleon, 14 sickles, 1 knuts
print(convert_knuts(544)) #Expected: 1 galleon, 4 sickles, 18 knuts
print(convert_knuts(993)) #Expected: 2 galleons 7 knuts SHOULDN'T show any sickles
'''



#Question 2:  Debugger_p2_HighwayNumbers - Finished debugging

def highway_directions(highway_num):
	if 1 < highway_num < 99:
		if highway_num % 2 == 0:
			return f"I-{highway_num} runs east/west"
		else: #Swapped these two f strings.
			return f"I-{highway_num} runs north/south"

	elif 100 < highway_num < 999: #Changes <= to < 
		service_highway = highway_num % 100

		if 1 <= service_highway <= 99:
			if service_highway % 2 == 0:
				return f"I-{highway_num} runs east/west"
			else: #Removed the elif and just put else.
				return f"I-{highway_num} runs north/south"
		else:
			return f"I-{highway_num} is an invalid highway number"
	else:
		return f"I-{highway_num} is an invalid highway number"
'''
print(highway_directions(5))
print(highway_directions(82))
print(highway_directions(200))
print(highway_directions(353))
'''

#Question 3: Rugs: finished debugging

def design_rug(width, length, pattern = '@'): #Error 1: added @
	result = "Your rug is:\n"
	for i in range(length): #Error 3, removed the '-1' for length
		result += pattern * width
		if i < length - 1:
			result += "\n" #Error 2, switched '\t' to '\n'
	return result
'''
print(design_rug(3, 5, '$'))
print(design_rug(16, 5))
'''


#Question 4: Complete

def count_duplicates(num_1, num_2, num_3):
	count = 0
	
	if num_1 == num_2 == num_3: #Added condition for all equal
		return "You entered the same number 3 times"
	if num_1 == num_2:
		count += 1

	if num_1 == num_3:
		count += 1
	if num_2 == num_3: #Error 1: Was originally elif num1 == num3
		count += 1 #Added a '+' to the "+="
	
	if count == 0: #Edited from 1 to 0
		return "Each number is unique"
	#elif count == 3:					redundant code. Edited out
	#	return "You entered the same number 3 times"
	else:
		return "You entered the same number 2 times"
'''
print(count_duplicates(2, 3, 2))
print(count_duplicates(4, 4, 4))
print(count_duplicates(1, 2, 3))
'''

#Question 5: FlipFlop: no idea what's wrong here.

def flip_flop(word):
	length = len(word)
	middle = length // 2

	if length // 2 == 0:
		first_half = word[middle:]
		second_half = word[middle:]
		return second_half + first_half
	else:
		first_part = word[:middle]
		middle_char = word[middle]
		last_part = word[middle+1:]
		return last_part + middle_char + first_part
'''
print(flip_flop('abcd'))
print(flip_flop('grapes'))
print(flip_flop('abcde'))
print(flip_flop('cranberries'))
'''













#10 Find Factors - incomplete

def find_factors(num):
	factors = []
	
	for i in range(1, num):
		if num % i != 0: #Possible error 2: this code only adds odd numbers to a list
			factors.append(i) #Possible error 1: used to be .add(i)

	return factors
'''
print(find_factors(12)) #Expected: [1,2,3,4,6,12]
print(find_factors(17)) #Expected: [1,17]
print(find_factors(36)) #Expected: [1,2,3,4,6,9,12,18,36]
'''






#12 Game- odd or even - Finished debugging

from random import randint #Error 1: ranting was 'randominteger'

def guess(guess="odd"):
	value = randint(0, 9)
	
	if value // 2 == 0:
		actual = "even"
	else:
		actual = "odd"
	
	if guess == actual:
		return "Correct!"
	else:
		return "Incorrect!"

'''
print('\nFinal result: '+ guess()) #Expected: Correct if odd
print(40*'-')#Separator for clarity
print('\nFinal result: '+ guess('odd'+'\n')) #Expected: Correct if odd
print(40*'-')#Separator for clarity
print('\nFinal result: '+ guess('even'+'\n')) #Expected: Correct if even
print(40*'-')#Separator for clarity
'''















