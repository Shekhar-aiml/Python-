""" For Loop
For loops is used to iterate over a sequence such as a list, tuple, string or range.
It executes a block of code once for each item in the sequence. """

#example 
for i in range(1,11)
   print(i)

#question

""" The current population of a town is 10000. 
The population of the town is increasing at the rate of 10% per year. 
You have to write a program to find out the population at the end of each of the last 10 years. """

curr_pop = 10000

for i in range(10,0,-1):
    print(i,curr_pop)

    curr_pop = curr_pop / 1.1

# Sequence sum
# 1/1! + 2/2! + 3/3! + ...'

n = int(input('Enter n: '))

result = 0
fact = 1

for i in range (1,n + 1): 
    
    fact = fact * i
    result = result + i / fact
    

print(result)



