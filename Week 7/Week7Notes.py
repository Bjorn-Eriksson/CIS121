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

#print(__name__)
#prints '__main__', because we're currently writing in the main space.


#When a function is invoked, python creates a local namespace corresponding
# to the function itself.

#Once the funciton is completed, the local namespace is destroyed. 
# This is done through a process called garbage collection
# Refer to W7 D1 notebook page.
# The red stuff is deleted.

#When we try to import the math module using import math, python
# creates a namespace with a reference to the new namespace
# for the module itself. This looks like... (Refer to W7D1 notebook, fig. 2)























































