# Python Keywords
"""
Keywords in Python are special reserved words that are part of the language itself.
 They define the rules and structure of Python programs which means you cannot use them 
 as names for your variables,functions, classes or any other identifiers.

Getting List of all Python keywords
We can also get all the keyword names using the below code.

"""
import keyword
print("The list of keywords are : ")
print(keyword.kwlist)


"""Identify Python Keywords
Ways to identify Python Keywords are:

With Syntax Highlighting: Most of IDEs provide syntax-highlight feature. 
You can see Keywords appearing in different color or style.

Look for SyntaxError: This error will encounter if you have used any keyword incorrectly.
 Keywords can not be used as identifiers like variable or a function name."""



#Python Identifiers 
"""
Python Identifiers are user-defined names for variables, functions, or classes. 
Must follow naming rules (no digits at start, only _ allowed)."""


"""Identifiers in Python
User-defined names for variables, functions, classes, modules, etc.
Can include letters, digits, and underscores (_).
Case-sensitive → num, Num, and NUM are different identifiers.
Python provides str.isidentifier() to check if a string is a valid identifier.
Rules for Naming Python Identifiers
It cannot be a reserved python keyword.
It should not contain white space.
It can be a combination of A-Z, a-z, 0-9, or underscore.
It should start with an alphabet character or an underscore ( _ ).
It should not contain any special character other than an underscore ( _ ).
Examples of Python Identifiers"""

#Valid identifiers:
"""
var1
_var1 
_1_var

"""
#Invalid Identifiers

"""!var1
1var
1_var
var#1
var 1"""
