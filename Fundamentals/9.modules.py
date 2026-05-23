"""
Python Modules

Module is a file containing definitions and statements. A module can define functions, classes and variables.
Modules help organize code into separate files so that programs become easier to maintain and reuse. 
Instead of writing everything in one place, related functionality can be grouped into its own module and imported whenever needed.

Create a Module
To create a module, write the desired code and save that in a file with .py extension.

Example: Let's create a calc.py in which we define two functions, one add and another subtract."""

# calc.py
def add(x, y):
    return (x+y)

def subtract(x, y):
    return (x-y)

import calc
print(calc.add(10, 2)) #Example

#import module
from math import sqrt, factorial
print(sqrt(16))
print(factorial(6))
