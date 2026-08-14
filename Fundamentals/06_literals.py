"""
Python Literals
================

A literal is a value written directly in Python source code.

Examples:

    10
    3.14
    "Python"
    True
    None

Python supports several kinds of literals:

- Numeric literals
- String literals
- Boolean literals
- None literal
"""


# ============================================================
# 1. Numeric Literals
# ============================================================
"""
Numeric literals represent numbers directly in source code.

Python supports:

- Integer literals
- Floating-point literals
- Complex literals
"""


# ------------------------------------------------------------
# 1.1 Integer Literals
# ------------------------------------------------------------
"""
Integer literals can be written in different number systems:

- Decimal  -> base 10
- Binary   -> base 2
- Octal    -> base 8
- Hex      -> base 16
"""

binary_number = 0b1010
decimal_number = 100
octal_number = 0o310
hexadecimal_number = 0x12C

print("Binary:", binary_number)
print("Decimal:", decimal_number)
print("Octal:", octal_number)
print("Hexadecimal:", hexadecimal_number)


# ------------------------------------------------------------
# 1.2 Floating-Point Literals
# ------------------------------------------------------------

float_1 = 10.5
float_2 = 1.5e2       # 1.5 × 10²
float_3 = 1.5e-3      # 1.5 × 10⁻³

print("\nFloating-Point Literals:")
print(float_1)
print(float_2)
print(float_3)


# ------------------------------------------------------------
# 1.3 Complex Literals
# ------------------------------------------------------------

complex_number = 3.14j

print("\nComplex Literal:")
print(complex_number)
print("Real part:", complex_number.real)
print("Imaginary part:", complex_number.imag)


# ============================================================
# 2. String Literals
# ============================================================
"""
Strings represent text in Python.

Strings can be created using:

- Single quotes
- Double quotes
- Triple quotes
"""


# ------------------------------------------------------------
# 2.1 Single and Double Quotes
# ------------------------------------------------------------

single_quote_string = 'This is Python'
double_quote_string = "This is Python"

print("\nString Literals:")
print(single_quote_string)
print(double_quote_string)


# ------------------------------------------------------------
# 2.2 No Separate Character Type
# ------------------------------------------------------------
"""
Python does not have a separate character type.

A single character is simply a string of length 1.
"""

character = "C"

print("\nCharacter:")
print(character)
print(type(character))
print(len(character))


# ------------------------------------------------------------
# 2.3 Multiline String
# ------------------------------------------------------------

multiline_string = """
This is a
multiline string.
"""

print("\nMultiline String:")
print(multiline_string)


# ------------------------------------------------------------
# 2.4 Unicode String
# ------------------------------------------------------------
"""
Python strings support Unicode characters.
"""

unicode_string = "\U0001F600 \U0001F606 \U0001F923"

print("\nUnicode String:")
print(unicode_string)


# ------------------------------------------------------------
# 2.5 Raw String
# ------------------------------------------------------------
"""
Raw strings treat backslashes as literal characters
for most escape sequences.

Useful when working with paths and regular expressions.
"""

raw_string = r"raw \n string"

print("\nRaw String:")
print(raw_string)


# ============================================================
# 3. Boolean Literals
# ============================================================
"""
Python has two Boolean literals:

- True
- False
"""

is_python_fun = True
is_python_boring = False

print("\nBoolean Literals:")
print(is_python_fun)
print(type(is_python_fun))

print(is_python_boring)
print(type(is_python_boring))


# ------------------------------------------------------------
# 3.1 Boolean Values Behave Like Integers
# ------------------------------------------------------------
"""
bool is a subclass of int in Python.

Therefore:

    True  -> 1
    False -> 0
"""

true_result = True + 4
false_result = False + 10

print("\nBoolean Arithmetic:")
print("True + 4 =", true_result)
print("False + 10 =", false_result)


# ============================================================
# 4. None
# ============================================================
"""
None represents the absence of a value.

It is commonly used when:

- A value does not exist yet.
- A function does not explicitly return a value.
- We want to represent "no value".
"""

result = None

print("\nNone:")
print(result)
print(type(result))


# ============================================================
# 5. Literal vs Variable
# ============================================================
"""
A literal is the actual value written in the source code.

Example:

    age = 25

Here:

    age -> identifier / variable name
    25  -> integer literal
"""

age = 25
name = "Alice"
active = True
value = None

print("\nLiteral Examples:")
print(age)
print(name)
print(active)
print(value)


# ============================================================
# Summary
# ============================================================
"""
Common Python literals:

Integer:
    100
    0b1010
    0o310
    0x12C

Float:
    10.5
    1.5e2

Complex:
    3 + 4j

String:
    "Python"
    'Python'
    """ + '"""' + """multiline""" + '"""' + """

Boolean:
    True
    False

None:
    None
"""
