"""
Python While Loop
=================

A while loop repeatedly executes a block of code as long as
its condition remains True.

Syntax:

    while condition:
        statement

The condition is checked before every iteration.

When the condition becomes False, execution continues with
the statement immediately after the loop.
"""


# ============================================================
# 1. Basic While Loop
# ============================================================

i = 1

while i <= 5:
    print(i)
    i += 1


# ============================================================
# 2. While Loop with User Input
# ============================================================
"""
Example:
Print the multiplication table of a number.
"""

number = int(input("\nEnter a number: "))

i = 1

while i <= 10:
    print(number, "*", i, "=", number * i)
    i += 1


# ============================================================
# 3. Guessing Game
# ============================================================
"""
The program generates a random number between 1 and 10.

The user keeps guessing until the correct number is entered.
"""

import random


jackpot = random.randint(1, 10)

guess = int(input("\nGuess the number (1-10): "))

attempts = 1

while guess != jackpot:

    if guess < jackpot:
        print("Guess higher.")
    else:
        print("Guess lower.")

    guess = int(input("Guess again: "))
    attempts += 1

print("Correct!")
print("Attempts:", attempts)


# ============================================================
# 4. Important: Avoid Infinite Loops
# ============================================================
"""
A while loop must eventually make its condition False.

Example:

    i = 1

    while i <= 5:
        print(i)
        i += 1

If i += 1 is removed, the condition remains True
and the loop becomes infinite.
"""
