#Python String

""" Strings are sequence of characters written inside quotes. It can include letters, numbers, symbols and spaces.
Python does not have a separate character type.

A single character is treated as a string of length one.
Strings are commonly used for text handling and manipulation.
Creating a String
Strings can be created using either single ('...') or double ("...") quotes. Both behave the same.
"""

#Example 
s = 'Hello World'
s = "It's raining outside"

s = '''Multiline String'''
s = """Multiline String """


# ==========================================================
# Accessing Characters in a String in Python
# ==========================================================

s = "hello world"


# ==========================================================
# Positive Indexing
# ==========================================================

print("Positive Indexing")

print(s[0])   # h
print(s[1])   # e
print(s[5])   # (space)

print("-" * 50)


# ==========================================================
# Negative Indexing
# ==========================================================

print("Negative Indexing")

print(s[-1])  # d
print(s[-4])  # o

print("-" * 50)


# ==========================================================
# String Slicing
# ==========================================================

print("String Slicing")

# Positive slicing
print(s[0:5])     # hello
print(s[3:6])     # lo
print(s[0:6:2])   # hlo

# Reverse slicing
print(s[6:0:-1])  # w olle

print("-" * 50)


# ==========================================================
# Reversing a String
# ==========================================================

print("Reversing String")

print(s[::-1])    # dlrow olleh

print("-" * 50)


# ==========================================================
# Negative Slicing
# ==========================================================

print("Negative Slicing")

print(s[-1:-6:-1])   # dlrow

print("-" * 50)


# ==========================================================
# Editing Strings
# ==========================================================

# Python strings are immutable.
# You cannot modify individual characters.

# Example:
# s[0] = 'H'    Error


# ==========================================================
# Deleting a String
# ==========================================================

del s

# print(s)    NameError: 's' is deleted


# ==========================================================
# Operations on Strings
# ==========================================================

print("\nOperations on Strings\n")


# ==========================================================
# Arithmetic Operations
# ==========================================================

print("Arithmetic Operations")

# Concatenation
print("Mumbai" + " " + "Delhi")

# Repetition
print("*" * 50)

print("-" * 50)


# ==========================================================
# Relational Operators
# ==========================================================

print("Relational Operators\n")

print("Mumbai" < "Pune")
print("pune" > "mumbai")

print("mumbai" == "pune")
print("mumbai" != "pune")

print("-" * 50)


# ==========================================================
# Logical Operators
# ==========================================================

print("Logical Operators\n")

print("hello" and "world")
print("hello" or "world")
print("" or "world")

print("-" * 50)


# ==========================================================
# Membership Operators
# ==========================================================

print("Membership Operators")

print("D" in "Delhi")
print("d" not in "delhi")

print("-" * 50)


# ==========================================================
# Loops in Strings
# ==========================================================

print("Loops in Strings")

for i in "hello":
    print(i)

print("-" * 50)

for i in "delhi":
    print("pune")


#functions on strings 

len('hello world')   #shows length of strings
max('hello world')   #maximum string 
min('hello world')     #minimum
sorted('hello world')   #sorts in ascending order



#Capitalize/title/Uppercase/lowercase/swapcase

s = 'hello world'

print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.swapcase()) 

# Search & Count Methods
# ------------------------------------------

s = "Hello Everyone"

print("Count of 'o':", s.count('o'))
print("Find 'y':", s.find('y'))      # Returns -1 if not found
print("Index of 'o':", s.index('o')) # Raises error if not found

print("-" * 50)


# ------------------------------------------
# String Checking Methods
# ------------------------------------------

s = "my name is tony stark"

print("Starts with 'my':", s.startswith('my'))
print("Ends with 'stark':", s.endswith('stark'))

print("-" * 50)


# ------------------------------------------
# String Formatting
# ------------------------------------------

name = "tony"
age = 25

print("My name is {}, and my age is {}".format(name, age))

print("-" * 50)


# ------------------------------------------
# Validation Methods
# ------------------------------------------

username = "tony125"

print("isalnum():", username.isalnum())          # Letters + numbers
print("isalpha():", username.isalpha())          # Only letters
print("isdigit():", username.isdigit())          # Only digits
print("isidentifier():", username.isidentifier()) # Valid variable name

print("-" * 50)


# ------------------------------------------
# Split & Join Methods
# ------------------------------------------

text = "once upon a time"

print("split():", text.split())
print("join():", "-".join(["once", "upon", "a", "time"]))

print("-" * 50)


