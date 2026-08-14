"""
Python Operators
================

Operators are symbols or keywords used to perform operations
on values and variables.

Python provides several types of operators:

1. Arithmetic Operators
2. Comparison Operators
3. Logical Operators
4. Bitwise Operators
5. Assignment Operators
6. Membership Operators
7. Identity Operators
"""


# ============================================================
# Getting Input
# ============================================================

print("Enter two numbers to perform operations:\n")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))


# ============================================================
# 1. Arithmetic Operators
# ============================================================
"""
Arithmetic operators are used to perform mathematical operations.

+   Addition
-   Subtraction
*   Multiplication
/   Division
//  Floor Division
%   Modulus
**  Exponentiation
"""

print("\nArithmetic Operators:")

print("a + b  =", a + b)
print("a - b  =", a - b)
print("a * b  =", a * b)
print("a / b  =", a / b)
print("a // b =", a // b)
print("a % b  =", a % b)
print("a ** b =", a ** b)


# ============================================================
# 2. Comparison Operators
# ============================================================
"""
Comparison operators compare two values.

The result is always True or False.

>   Greater than
<   Less than
>=  Greater than or equal to
<=  Less than or equal to
==  Equal to
!=  Not equal to
"""

print("\nComparison Operators:")

print("a > b  =", a > b)
print("a < b  =", a < b)
print("a >= b =", a >= b)
print("a <= b =", a <= b)
print("a == b =", a == b)
print("a != b =", a != b)


# ============================================================
# 3. Logical Operators
# ============================================================
"""
Logical operators are commonly used with Boolean expressions.

and -> True if both conditions are True
or  -> True if at least one condition is True
not -> Reverses a Boolean value
"""

print("\nLogical Operators:")

print("a > 0 and b > 0:", a > 0 and b > 0)
print("a > 0 or b > 0 :", a > 0 or b > 0)
print("not (a > 0)    :", not (a > 0))


# ============================================================
# 4. Bitwise Operators
# ============================================================
"""
Bitwise operators work on the binary representation of integers.

&   AND
|   OR
^   XOR
~   NOT
>>  Right Shift
<<  Left Shift
"""

print("\nBitwise Operators:")

print("a & b  =", a & b)
print("a | b  =", a | b)
print("a ^ b  =", a ^ b)
print("~a     =", ~a)
print("a >> b =", a >> b)
print("a << b =", a << b)


# ============================================================
# 5. Assignment Operators
# ============================================================
"""
Assignment operators are used to assign or update values.

=    Assignment
+=   Add and assign
-=   Subtract and assign
*=   Multiply and assign
/=   Divide and assign
//=  Floor divide and assign
%=   Modulus and assign
**=  Exponentiate and assign

The variable x is used so that the original value of a
remains unchanged.
"""

print("\nAssignment Operators:")

x = a

x += b
print("x += b:", x)

x -= b
print("x -= b:", x)

x *= b
print("x *= b:", x)

x /= b
print("x /= b:", x)

x //= b
print("x //= b:", x)

x %= b
print("x %= b:", x)

x **= b
print("x **= b:", x)


# ============================================================
# 6. Membership Operators
# ============================================================
"""
Membership operators check whether a value exists
inside a sequence or collection.

in      -> True if the value exists
not in  -> True if the value does not exist
"""

print("\nMembership Operators:")

city = "Delhi"

print("'D' in city     =", "D" in city)
print("'D' not in city =", "D" not in city)
print("'x' in city     =", "x" in city)


# ============================================================
# 7. Identity Operators
# ============================================================
"""
Identity operators check whether two variables refer to
the same object.

is      -> Same object
is not  -> Different objects

Do not confuse 'is' with '=='.

== checks whether values are equal.
is checks whether objects are the same object.
"""

x = [1, 2, 3]
y = x
z = [1, 2, 3]

print("\nIdentity Operators:")

print("x == y:", x == y)
print("x is y:", x is y)

print("x == z:", x == z)
print("x is z:", x is z)
