"""
Python Nested Loops
===================

A nested loop is a loop placed inside another loop.

The inner loop executes completely for every iteration
of the outer loop.

Nested loops can be created using:

- for inside for
- while inside while
- for inside while
- while inside for

Syntax:

    for outer_variable in iterable:
        for inner_variable in iterable:
            statement
"""


# ============================================================
# 1. Basic Nested For Loop
# ============================================================
"""
The inner loop runs completely for every iteration
of the outer loop.
"""

for i in range(1, 5):

    for j in range(1, 5):
        print(i, j)


# ============================================================
# 2. Star Pattern
# ============================================================
"""
Pattern:

*
**
***
****
"""

rows = int(input("\nEnter the number of rows: "))

for i in range(1, rows + 1):

    for j in range(1, i + 1):
        print("*", end="")

    print()


# ============================================================
# 3. Number Pattern
# ============================================================
"""
Pattern:

1
121
12321
1234321
"""

rows = int(input("\nEnter the number of rows: "))

for i in range(1, rows + 1):

    # Increasing numbers
    for j in range(1, i + 1):
        print(j, end="")

    # Decreasing numbers
    for j in range(i - 1, 0, -1):
        print(j, end="")

    print()


# ============================================================
# 4. How the Number Pattern Works
# ============================================================
"""
For i = 4:

First loop:

    1 2 3 4

Second loop:

    3 2 1

Combined:

    1234321
"""
