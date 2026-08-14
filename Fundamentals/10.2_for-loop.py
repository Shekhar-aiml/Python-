"""
Python For Loop
===============

A for loop is used to iterate over an iterable such as:

- List
- Tuple
- String
- Range
- Set
- Dictionary

The loop executes once for each item in the iterable.

Syntax:

    for variable in iterable:
        statement
"""


# ============================================================
# 1. Basic For Loop
# ============================================================

for i in range(1, 11):
    print(i)


# ============================================================
# 2. Iterating Over a String
# ============================================================

name = "Python"

for character in name:
    print(character)


# ============================================================
# 3. Iterating Over a List
# ============================================================

languages = ["Python", "Java", "C++"]

for language in languages:
    print(language)


# ============================================================
# 4. Using range()
# ============================================================
"""
range() generates a sequence of numbers.

range(start, stop)

The stop value is excluded.

Example:

    range(1, 6)

produces:

    1, 2, 3, 4, 5
"""

for i in range(1, 6):
    print(i)


# ============================================================
# 5. range() with Step
# ============================================================

for i in range(10, 0, -1):
    print(i)


# ============================================================
# 6. Population Problem
# ============================================================
"""
Problem:

The current population of a town is 10,000.

The population increases by 10% every year.

Find the population at the end of each of the previous
10 years.

We work backwards by dividing the current population
by 1.1 for each previous year.
"""

current_population = 10000

for year in range(10, 0, -1):
    print(f"{year} years ago: {current_population:.2f}")

    current_population = current_population / 1.1


# ============================================================
# 7. Series Sum
# ============================================================
"""
Calculate:

1/1! + 2/2! + 3/3! + ... + n/n!

The factorial is calculated progressively inside the loop.
"""

n = int(input("\nEnter n: "))

result = 0
factorial = 1

for i in range(1, n + 1):

    factorial *= i
    result += i / factorial

print("Result:", result)
