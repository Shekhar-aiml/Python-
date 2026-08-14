"""
Python Modules
==============

A module is a Python file containing definitions and statements.

A module can contain:

- Functions
- Classes
- Variables

Modules help us:

- Organize code
- Reuse code
- Keep related functionality together
- Make programs easier to maintain

A Python module is simply a .py file.
"""


# ============================================================
# 1. Creating a Module
# ============================================================
"""
Suppose we have a file named:

    calc.py

The calc.py module contains:

    add()
    subtract()

We can import the module and use its functions.
"""

import calc


print("Using the calc module:")

print("Addition:", calc.add(10, 2))
print("Subtraction:", calc.subtract(10, 2))


# ============================================================
# 2. Importing Specific Functions
# ============================================================
"""
Instead of importing the entire module, we can import
specific functions from a module.
"""

from math import sqrt, factorial


print("\nUsing specific functions from math:")

print("Square root:", sqrt(16))
print("Factorial:", factorial(6))


# ============================================================
# 3. Importing the Entire Module
# ============================================================
"""
We can also import the entire math module.

Example:

    import math

Then access functions using:

    math.sqrt()
    math.factorial()
"""

import math


print("\nUsing the math module:")

print("Square root:", math.sqrt(25))
print("Factorial:", math.factorial(5))


# ============================================================
# 4. Importing with an Alias
# ============================================================
"""
The 'as' keyword allows us to give a module a shorter name.

Example:

    import math as m
"""

import math as m

print("\nUsing an alias:")
print("Square root:", m.sqrt(36))


# ============================================================
# 5. Module Naming
# ============================================================
"""
When importing your own module:

    import calc

Python looks for calc.py in the appropriate module search path.

Avoid naming your own modules after standard-library modules.

For example, avoid names such as:

    math.py
    random.py
    os.py

because they can cause import conflicts.
"""
