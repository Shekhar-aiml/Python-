"""
Python Conditional Statements
==============================

Conditional statements allow a program to make decisions
based on whether a condition is True or False.

Python provides:

- if
- if-else
- if-elif-else
- Nested if statements

Basic structure:

    if condition:
        statement
    elif condition:
        statement
    else:
        statement
"""


# ============================================================
# 1. if Statement
# ============================================================
"""
The if statement executes a block of code only when
the condition is True.
"""

age = 20

if age >= 18:
    print("You are eligible to drive.")


# ============================================================
# 2. if-else Statement
# ============================================================
"""
The if-else statement provides two possible paths.

If the condition is True:
    if block executes.

If the condition is False:
    else block executes.
"""

age = int(input("\nEnter your age: "))

if age >= 18:
    print("You are eligible for a driving license.")
else:
    print("You are not eligible for a driving license.")


# ============================================================
# 3. if-elif-else Statement
# ============================================================
"""
The elif keyword allows us to check multiple conditions.

Python checks conditions from top to bottom.
The first True condition is executed.
"""

marks = int(input("\nEnter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 40:
    print("Grade: D")
else:
    print("Grade: F")


# ============================================================
# 4. Nested if Statement
# ============================================================
"""
An if statement can be placed inside another if statement.

This is called a nested if statement.
"""

email = input("\nEnter your email: ")
password = input("Enter your password: ")

if email == "example@gmail.com":
    if password == "1221":
        print("Login successful.")
    else:
        print("Incorrect password.")
else:
    print("Login failed.")


# ============================================================
# 5. Multiple Conditions
# ============================================================
"""
Logical operators can be used with conditional statements.

    and -> Both conditions must be True.
    or  -> At least one condition must be True.
    not -> Reverses the condition.
"""

age = int(input("\nEnter your age: "))
has_license = input("Do you have a driving license? (yes/no): ")

if age >= 18 and has_license == "yes":
    print("You can drive.")
else:
    print("You cannot drive.")


# ============================================================
# 6. Menu-Driven Program
# ============================================================
"""
Conditional statements can be used to create
menu-driven programs.
"""

menu = int(
    input(
        """
How can I help you?

1. Change PIN
2. Check Balance
3. Withdraw

Enter your choice: """
    )
)

if menu == 1:
    print("Change PIN selected.")
elif menu == 2:
    print("Check Balance selected.")
elif menu == 3:
    print("Withdraw selected.")
else:
    print("Invalid choice.")


# ============================================================
# 7. Find Minimum of Three Numbers
# ============================================================
"""
Exercise:
Find the smallest of three numbers using
conditional statements.
"""

a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a <= b and a <= c:
    smallest = a
elif b <= a and b <= c:
    smallest = b
else:
    smallest = c

print("Smallest number:", smallest)
