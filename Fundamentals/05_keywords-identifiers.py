"""
Python Keywords and Identifiers
================================

Keywords are reserved words that have a special meaning in Python.
They are part of Python's syntax and cannot normally be used as
names for variables, functions, classes, or other identifiers.

Identifiers are user-defined names used to identify objects such as
variables, functions, classes, and modules.
"""

import keyword


# ============================================================
# 1. Python Keywords
# ============================================================
"""
Python keywords are reserved words with predefined meanings.

Examples:

    if
    else
    for
    while
    def
    class
    return
    import
    True
    False
    None

Keywords cannot be used as normal identifiers.
"""


# ------------------------------------------------------------
# 1.1 Get All Python Keywords
# ------------------------------------------------------------

print("Python Keywords:")
print(keyword.kwlist)


# ------------------------------------------------------------
# 1.2 Check Whether a Word Is a Keyword
# ------------------------------------------------------------

word = "for"

print(f"\nIs '{word}' a keyword?")
print(keyword.iskeyword(word))


word = "python"

print(f"Is '{word}' a keyword?")
print(keyword.iskeyword(word))


# ============================================================
# 2. Python Identifiers
# ============================================================
"""
Identifiers are names created by the programmer.

They can be used for:

- Variables
- Functions
- Classes
- Modules
- Objects

Examples:

    name
    age
    calculate_total
    Student
    my_module
"""


# ============================================================
# 3. Rules for Python Identifiers
# ============================================================
"""
Rules:

1. An identifier can contain letters, digits, and underscores.
2. An identifier cannot start with a digit.
3. An identifier cannot contain spaces.
4. An identifier cannot contain special characters.
5. An identifier cannot be a Python keyword.
6. Identifiers are case-sensitive.
"""


# ------------------------------------------------------------
# 3.1 Valid Identifiers
# ------------------------------------------------------------

name = "Alice"
age1 = 25
_user_name = "Bob"
student_01 = "John"
_1_student = "David"

print("\nValid Identifiers:")
print(name)
print(age1)
print(_user_name)
print(student_01)
print(_1_student)


# ------------------------------------------------------------
# 3.2 Invalid Identifiers
# ------------------------------------------------------------

"""
The following are invalid identifiers:

1var        -> Cannot start with a digit
1_var       -> Cannot start with a digit
var#1       -> Special character is not allowed
var 1       -> Spaces are not allowed
for         -> Python keyword
"""


# ============================================================
# 4. Identifier Naming Examples
# ============================================================

first_name = "Alice"
student_age = 20

print("\nNaming Examples:")
print(first_name)
print(student_age)


# ============================================================
# 5. Case Sensitivity
# ============================================================
"""
Python identifiers are case-sensitive.

The following are three different identifiers:

    name
    Name
    NAME
"""

name = "Alice"
Name = "Bob"
NAME = "Charlie"

print("\nCase Sensitivity:")
print(name)
print(Name)
print(NAME)


# ============================================================
# 6. Check Whether a String Is a Valid Identifier
# ============================================================
"""
Python provides str.isidentifier() to check whether
a string follows the basic rules for an identifier.

Note:

isidentifier() does not check whether the string is a keyword.
For example, "for".isidentifier() is True, but "for" is
still not valid as a normal identifier because it is a keyword.
"""

valid_name = "student_name"
invalid_name = "student-name"

print("\nIdentifier Validation:")

print(valid_name.isidentifier())
print(invalid_name.isidentifier())


# ============================================================
# 7. Keyword + Identifier Validation
# ============================================================

name = "student_name"

print("\nIs the name valid?")

if name.isidentifier() and not keyword.iskeyword(name):
    print(f"'{name}' is a valid Python identifier.")
else:
    print(f"'{name}' is not a valid Python identifier.")


# ============================================================
# 8. Keywords vs Identifiers
# ============================================================
"""
Keyword:

    A reserved word defined by Python.

Identifier:

    A name created by the programmer.

Example:

    class Student:
        pass

'class'   -> Keyword
'Student' -> Identifier
"""


class Student:
    pass


print("\nKeyword vs Identifier:")
print(Student)
