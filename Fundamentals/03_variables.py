"""
Python Variables

A variable is a named reference to a value. Variables are used to store
and manipulate data during program execution.

Key Points:
- No explicit type declaration is required.
- Python is dynamically typed.
- Variable names are case-sensitive.
"""


# Creating Variables


age = 21
name = "Alex"
height = 5.9
is_student = True

print(age)
print(name)
print(height)
print(is_student)


# Variable Naming Rules


student_name = "John"     # Valid
_total = 500              # Valid
marks2 = 95               # Valid

# Invalid Examples
# 2marks = 95             # Cannot start with a digit
# user-name = "John"      # Hyphen not allowed
# class = "Python"        # Keyword cannot be used


# Dynamic Typing


x = 100
print(x, type(x))

x = "Python"
print(x, type(x))


# Multiple Assignment


a = b = c = 10
print(a, b, c)

x, y, z = 1, 2.5, "Hello"
print(x, y, z)


# Variable Swapping
x = 5
y = 10

x, y = y, x

print(x, y)


# Type Checking


price = 99.99

print(type(price))
print(type(name))

# Object Identity


num = 100
copy_num = num

print(id(num))
print(id(copy_num))


# Deleting Variables


temp = "Temporary"

del temp

# print(temp)   # NameError


# Best Practices


first_name = "Alice"
total_marks = 480
is_passed = True

print(first_name)
print(total_marks)
print(is_passed)


