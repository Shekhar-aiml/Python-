"""
Python Loop Control Statements
==============================

Loop control statements change the normal execution of a loop.

Python provides three commonly used loop control statements:

1. break
2. continue
3. pass
"""


# ============================================================
# 1. break Statement
# ============================================================
"""
The break statement immediately terminates the loop.

Execution continues with the first statement after the loop.
"""


# ------------------------------------------------------------
# 1.1 break with for Loop
# ------------------------------------------------------------

print("break with for loop:")

for i in range(5):

    if i == 3:
        break

    print(i)


# ------------------------------------------------------------
# 1.2 break with while Loop
# ------------------------------------------------------------

print("\nbreak with while loop:")

i = 0

while i < 5:

    if i == 3:
        break

    print(i)
    i += 1


# ============================================================
# 2. continue Statement
# ============================================================
"""
The continue statement skips the remaining code in the
current iteration and moves to the next iteration.
"""


# ------------------------------------------------------------
# 2.1 continue with for Loop
# ------------------------------------------------------------

print("\ncontinue example:")

for i in range(5):

    if i == 3:
        continue

    print(i)


# ------------------------------------------------------------
# 2.2 Practical Example
# ------------------------------------------------------------
"""
Print only the odd numbers from 1 to 10.
"""

print("\nOdd numbers:")

for i in range(1, 11):

    if i % 2 == 0:
        continue

    print(i)


# ============================================================
# 3. pass Statement
# ============================================================
"""
The pass statement does nothing.

It is used as a placeholder when Python requires
a statement syntactically, but we don't want to execute
any code yet.
"""


# ------------------------------------------------------------
# 3.1 pass in a Loop
# ------------------------------------------------------------

for i in range(5):

    if i == 3:
        pass

    print(i)


# ------------------------------------------------------------
# 3.2 pass in a Function
# ------------------------------------------------------------

def future_function():
    pass


# ============================================================
# 4. break vs continue vs pass
# ============================================================
"""
break
-----
Stops the entire loop.

continue
--------
Skips the current iteration and continues with the next one.

pass
----
Does nothing and allows execution to continue normally.
"""


# break
print("\nbreak:")

for i in range(5):

    if i == 3:
        break

    print(i)


# continue
print("\ncontinue:")

for i in range(5):

    if i == 3:
        continue

    print(i)


# pass
print("\npass:")

for i in range(5):

    if i == 3:
        pass

    print(i)
