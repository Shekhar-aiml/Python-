#Loop Control Statements

""" Loop control statements in Python are special statements that help control the execution of loops (for or while). 
They let you modify the default behavior of the loop, such as stopping it early, skipping an iteration, or doing nothing temporarily.
Python supports the following control statements: """

#Break statement
#Continue statement
#Pass statement


#Break Statement in Python
"""The break statement in Python is used to exit or “break” out of a loop (either a for or while loop) prematurely,
before the loop has iterated through all its items or reached its condition. 
When the break statement is executed, the program immediately exits the loop, and the control moves to the next line of code after the loop."""

#Example:

# Using For Loop
for i in range(5):
    if i == 3:
        break  # Exit the loop when i is 3
    print(i)
    
# Using While Loop
i = 0
while i < 5:
    if i == 3:
        break  # Exit the loop when i is 3
    print(i)
    i += 1


#Continue Statement in Python
""" Python Continue statement is a loop control statement that forces to execute the next iteration of the loop 
while skipping the rest of the code inside the loop for the current iteration only, i.e. 
when the continue statement is executed in the loop, the code inside the loop following the continue statement will be skipped for 
the current iteration and the next iteration of the loop will begin."""

#Example:
for i in range(5):
    if i == 3:
        continue  # Skip the rest of the code for i = 3
    print(i)
