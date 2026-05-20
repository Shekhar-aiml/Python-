"""
    Python Variables

Variables are used to store data that can be referenced and manipulated during program execution. A variable is essentially a name that is assigned to a value.

Unlike Java and many other languages, Python variables do not require explicit declaration of type.
Type of the variable is inferred based on the value assigned.

"""

x = 5
name = "Alex"  
print(x)
print(name) 

"""
Rules for Naming Variables
To use variables correctly, the following naming rules should be followed:

Names can contain letters, digits and underscores (_).
The first character cannot be a digit.
Names are case-sensitive, so myVar and myvar are treated differently.
Keywords such as if, else and for cannot be used as variable names.
Below listed variable names are valid:
"""

age = 21
_colour = "lilac"
total_score = 90

#Below listed variables names are invalid
class = 10       # class is a reserved keyword
user-name = "Doe"  # Contains a hyphen

#Assigning Values to Variables
# 1. Basic Assignment: Variables are assigned values using the = operator.


x = 5
y = 3.14
z = "Hi"

#2. Dynamic Typing: Python is dynamically typed, so the same variable can store different data types during execution.
x = 10
x = "Now a string"


#3. Assigning Same Value: same value can be assigned to multiple variables in a single line.
a = b = c = 100
print(a, b, c)


#4. Assigning Different Values: Multiple variables can also be assigned different values in a single line.

x, y, z = 1, 2.5, "Python"
print(x, y, z)


