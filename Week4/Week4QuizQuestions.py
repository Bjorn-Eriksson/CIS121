#Created by Bjorn Eriksson

#Question 1:

num1 = float(input("Enter a number: "))
num2 = float(input("Enter a second number: "))
divided = 0

while num1 > num2:
    if num1 /2 >= num2:
        divided += 1
        print(divided)
    elif num1 /2 <= num2:
        break
