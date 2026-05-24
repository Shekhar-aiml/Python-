#While Loop

"""While loop repeatedly executes a block of code as long as the given condition remains true. 
When the condition becomes false, the line immediately after the loop in the program is executed."""



#Table
number = int(input('Enter a number: '))

i = 1
while i<11:
    print(number,'*',i,'=',number*i)
    i +=1
