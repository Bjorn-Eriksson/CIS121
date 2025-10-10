#Created by Bjorn Eriksson

############ Day 1, Deep dive into how code works ##############
# A function is another data type with 2 operators.
# 1. Assignment = 
# 2. Invoking ()

#The parentheses are the operator that tells python to apply 
# the function to the supplied parameters.

def add_three(x):
    y = x + 3
    return y

var0 = 7
var1 = add_three(var0)

print(var1)
#Goal today is to understand how and why this works.

# In python, all names defined in a program are organized into namespaces.
# These are the names available when the program is executed.
# By default, python loads _ _builtin_ _(__builtin__) and _ _main_ _(__main__)

print(__name__)
#prints 'main', because we're currently writing in the main space.


















































