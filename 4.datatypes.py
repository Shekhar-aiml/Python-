"""Python Data Types

Data types are used to define the type of value stored in a variable. 
They determine what kind of operations can be performed on the data. 
In Python, everything is treated as an object and each value belongs to a specific data type. 
The following are standard or built-in data types in Python: """


#1 Numeric Data Types
"""
Numeric data types are used to store numeric values. 
It can be an integer, floating number or even a complex number.
 Python supports three main numeric types:

Integers: value is represented by int class. It contains positive or 
negative whole numbers (without fractions or decimals).

Float: value is represented by float class. It is a real number with a
 floating-point representation. It is specified by a decimal point.

Complex: It is represented by a complex class. 
It stores numbers with real and imaginary parts. For example: 2+3j

"""


a = 5
b = 5.0
c = 2 + 4j

print(type(a))
print(type(b))
print(type(c))


# Sequence Data Types

"""A sequence is an ordered collection of items, which can be of similar or 
different data types. Elements in a sequence can be accessed using indexing.

1. String

Strings are used to store text data. A string is represented using the str class and can be 
created using single, double or triple quotes.

"""


s = 'Welcome to the Geeks World'
print(s)
print(type(s))

# access string with index
print(s[1])
print(s[-1])

# 2.List

"""Lists are ordered and mutable collections used to store multiple items in a single variable. 
Elements in a list can be of different data types and are accessed using indexing."""


a = [1, 2, 3]
print(a)

b = ["Geeks", "For", "Geeks", 4, 5]
print(b[3])
print(b[-3])



# 3. Tuple
"""Tuples are ordered and immutable collections used to store multiple items in a single variable. Once created, tuple elements cannot be modified and are accessed using indexing.

Note: A tuple with a single element must include a trailing comma, otherwise Python treats it as a normal value instead of a tuple.
"""

t1 = (1,)
print(type(t1))

t2 = ('Geeks', 'For', 'Geeks', 1, 2)
print(t2[3])
print(t2[-3])

#4 Boolean Data Type
"""Boolean data type represents one of two values: True or False. It is mainly used in
conditions and comparisons and is represented by the bool class."""

print(type(True))
print(type(False))

#5 ruthy and Falsy Values
"""truthy and falsy values are values that evaluate to True or False in a Boolean context. 
Truthy values behave like True, while falsy values behave like False when used in conditions.
"""

if 1:
    print("1 is truthy")

if not 0:
    print("0 is falsy")


#6 Set Data Type
"""Sets are unordered and mutable collections used to store unique elements.
Since sets are unordered, elements cannot be accessed using indexing.
Elements are usually accessed by iterating through the set using a loop.
"""

s1 = {"a", "a", "b", "c", "b"}
print(s1)

s2 = {"Geeks", "For", "Geeks"}
for i in s2:
    print(i)

#7 Dictionary Data Type
"""Dictionaries are used to store data in key:value pairs.
Each key in a dictionary must be unique and values are accessed
using their keys with square brackets [] or get() method.

Note: Dictionary keys are case sensitive, the same name but 
different cases of Key will be treated distinctly. 

"""
d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(d[1])    
print(d.get(2))


#Imp know this

#Static vs Dynamic Typing?
"""Static vs Dynamic Typing
1. Dynamic Typing

In Python:

You do NOT fix the type of a variable
Type can change anytime

Example:
x = 10
x = "hello"

Allowed
Type changes

 Simple meaning:

“Same variable can hold different types”

2. Static Typing

In Java or C++:

 You MUST fix the type first
You cannot change it later

Example:
int x = 10;
x = "hello";  // ❌ error

 Not allowed

 Simple meaning:

“Variable type is fixed forever”
"""
#Static vs Dynamic Binding?

"""Static vs Dynamic Binding
1. Static Binding (Early Binding)

Decision is made before program runs

Used in:

Java
C++
Simple idea:

“Which function will run is already fixed early”

Example idea:
Call → already decided → run that function

Like:
You already know your classroom seat before entering.

2. Dynamic Binding (Late Binding)

Decision is made during program run

Used in:

Python
Simple idea:

“Which function will run is decided at runtime”

Example:
class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

animal = Dog()
animal.sound()

Now:

animal = Cat()
animal.sound()

Python decides at runtime:

Dog → Bark
Cat → Meow"""

#Stylish declaration techniques

"""
Stylish Declaration Techniques in Python

In Python, stylish declaration means writing variables in a clean and efficient way.

1. Multiple Assignment

Assign multiple values in one line:

a, b, c = 1, 2, 3

2. Same Value to Multiple Variables
x = y = z = 100

All variables store the same value.

3. Swapping Variables
a = 10
b = 20

a, b = b, a

No temporary variable needed.

4. List Unpacking
data = [1, 2, 3]

a, b, c = data

List elements are assigned to variables.

5. Extended Unpacking
nums = [1, 2, 3, 4, 5]

a, *middle, b = nums

print(a)
print(middle)
print(b)

Output:

1
[2, 3, 4]
5

6. Type Hint Style
name: str = "Rahul"
age: int = 20

Used for readability, not strict enforcement.

7. Dictionary Declaration
student = {
    "name": "Aman",
    "age": 21
}

8. List Declaration
fruits = ["apple", "banana", "mango"] """
