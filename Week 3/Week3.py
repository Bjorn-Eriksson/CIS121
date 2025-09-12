#Created by Bjorn Eriksson 

#Week 3 Quiz Questions

#Question 1:






#Question 5 
'''
num_1 = float(input("Enter number 1"))
num_2 = float(input("Enter number 2"))
num_3 = float(input("Enter number 3"))

#Starting code
if num_1 <= num_2 <= num_3:
    print(num_1, num_2, num_3)
elif num_1 <= num_3 <= num_2:
    print(num_1, num_3, num_2)
'''



#Question 6, Just reversing the order of Quesiton 5





#Question 7, using a lot of modulus (%)

#29 knuts = 1 sickle
#17 sickles = 1 galleon

#1 galleon = 493 Knuts


#Two ways to approach, top down or down up.

knuts = int(input("Enter amount of knuts: "))

#Find if we can buy any galleons
galleons = knuts // (29 * 17)
knuts_remaining = knuts % (29 * 17)

#See if we can buy sickles
sickles = knuts_remaining // 29
knuts_final = knuts_remaining % 29

message = ''
if galleons > 0:
    message += (f" Galleons : {galleons} ")
if sickles > 0:
    message += (f" Sickles : {sickles} ")
if knuts_remaining > 0:
    message += (f" Knuts : {knuts_final} ")

print(message)






