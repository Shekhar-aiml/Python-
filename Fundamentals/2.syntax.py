"""
Python Syntax

Syntax refers to the set of rules that define how Python code
must be written so that the interpreter can understand it.

Key Syntax Rules
----------------
1. Indentation defines code blocks.
2. Python is case-sensitive.
3. Colons (:) start a new code block.
4. Statements are usually written one per line.
5. Semicolons are optional but not recommended.
6. Comments begin with #.
7. Multi-line comments/docstrings use triple quotes.
"""


# Printing Output


print("Hello, World!")


# Indentation

if True:
    print("Indentation defines this block.")


# Statements


x = 10
y = 20
print(x + y)


# Comments


# This is a single-line comment.

"""
This is a multi-line comment
or documentation string (docstring).
"""


# Case Sensitivity

name = "Alice"

# print(Name)   # NameError
print(name)


# Colon (:)


for i in range(3):
    print(i)

# Optional Semicolon


a = 5
b = 10

# Valid but not recommended
c = a + b;
print(c)
