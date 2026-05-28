""" Python Nested Loops

In Python, there are two types of loops: for loop and while loop. Using these loops,
we can create nested loops, which means loops inside a loop. 
For example, a while loop inside a for loop, or a for loop inside another for loop."""

#Example 1
for i in range(1,5):
    for j in range(1,5):
        
        print(i,j)
      
#Example 2
#Pattern 1
"""
*
**
***
**** 
"""      

rows = int(input('Enter the number of rows: '))

for i in range (1,rows+1):
    for j in range (1,i+1):
        print('*',end='')
    print()       

#Example 3 
""" Print 
1
121
12321
1234321 
"""
rows = int(input('Enter the number of rows: '))

for i in range (1,rows+1):
    for j in range (1,i+1):
        print(j,end='')
    for k in range (i-1,0,-1): 
        print(k,end='')  
    print()        
  
      
      
