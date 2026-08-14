"""
Python Data Types
=================

Data types define the kind of value stored in an object.

Python has several built-in data types, including:

- Numeric: int, float, complex
- Sequence: str, list, tuple
- Boolean: bool
- Set: set
- Mapping: dict

Python is dynamically typed, meaning that a name does not need
an explicit type declaration and can later be bound to an object
of a different type.
"""


# ============================================================
# 1. Numeric Data Types
# ============================================================
"""
Python provides three main numeric types:

- int     -> whole numbers
- float   -> decimal/floating-point numbers
- complex -> real + imaginary numbers
"""

integer_number = 5
float_number = 5.0
complex_number = 2 + 4j

print(integer_number)
print(type(integer_number))

print(float_number)
print(type(float_number))

print(complex_number)
print(type(complex_number))


# ============================================================
# 2. Sequence Data Types
# ============================================================
"""
Sequence types are ordered collections.

Common sequence types:

- str
- list
- tuple

Elements can be accessed using indexing.
"""


# ------------------------------------------------------------
# 2.1 String
# ------------------------------------------------------------
"""
Strings are used to store text.

Strings can be created using:

- Single quotes
- Double quotes
- Triple quotes
"""

message = "Welcome to the Python World"

print(message)
print(type(message))

# Accessing characters using indexing
print(message[0])
print(message[1])
print(message[-1])


# ------------------------------------------------------------
# 2.2 List
# ------------------------------------------------------------
"""
Lists are ordered and mutable collections.

A list can contain elements of different data types.
"""

numbers = [1, 2, 3]

print(numbers)
print(type(numbers))

mixed_list = ["Python", "Java", 4, 5]

print(mixed_list)
print(mixed_list[2])
print(mixed_list[-1])

# Lists are mutable
numbers[0] = 100

print(numbers)


# ------------------------------------------------------------
# 2.3 Tuple
# ------------------------------------------------------------
"""
Tuples are ordered and immutable collections.

A tuple cannot be modified after it is created.

A single-element tuple requires a trailing comma.
"""

single_element_tuple = (1,)

print(single_element_tuple)
print(type(single_element_tuple))

languages = ("Python", "Java", "C++", "JavaScript")

print(languages)
print(languages[0])
print(languages[-1])


# ============================================================
# 3. Boolean Data Type
# ============================================================
"""
The bool type represents one of two values:

- True
- False

Booleans are commonly used in conditions and comparisons.
"""

is_python_easy = True
is_python_hard = False

print(is_python_easy)
print(type(is_python_easy))

print(is_python_hard)
print(type(is_python_hard))


# ============================================================
# 4. Truthy and Falsy Values
# ============================================================
"""
Values can be evaluated in a Boolean context.

Truthy values behave like True.
Falsy values behave like False.

Examples of commonly falsy values:

- 0
- False
- None
- ""
- []
- ()
- {}
"""


if 1:
    print("1 is truthy")


if not 0:
    print("0 is falsy")


# ============================================================
# 5. Set Data Type
# ============================================================
"""
Sets are unordered collections of unique elements.

Properties:

- Mutable
- No duplicate elements
- No indexing
"""

numbers_set = {1, 2, 3, 3, 2}

print(numbers_set)
print(type(numbers_set))


languages_set = {"Python", "Java", "Python", "C++"}

print(languages_set)

# Access set elements by iteration
for language in languages_set:
    print(language)


# ============================================================
# 6. Dictionary Data Type
# ============================================================
"""
Dictionaries store data in key-value pairs.

Example:

{
    key: value
}

Dictionary keys must be unique.
Keys are used to access their corresponding values.
"""

student = {
    "name": "Aman",
    "age": 21,
    "language": "Python",
}

print(student)
print(type(student))

# Access values using keys
print(student["name"])
print(student.get("age"))

# Dictionary keys are case-sensitive
person = {
    "Name": "Alice",
    "name": "Bob",
}

print(person["Name"])
print(person["name"])


# ============================================================
# 7. Checking Data Types
# ============================================================
"""
The type() function returns the type of an object.
"""

value = 100

print(type(value))


# ============================================================
# 8. Dynamic Typing
# ============================================================
"""
Python is dynamically typed.

A name does not need an explicit type declaration.

The same name can later be bound to an object
of a different type.
"""

value = 10

print(value)
print(type(value))

value = "Hello"

print(value)
print(type(value))

value = [1, 2, 3]

print(value)
print(type(value))
