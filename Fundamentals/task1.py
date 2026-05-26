#Q1 :- Print the given strings as per stated format.

"""Given strings:

"Data" "Science" "Mentorship" "Program" 
"By" "CampusX  """


print('Data','Science','Mentoship','Program','By','CampusX',sep='-')


#Q2:- Write a program that will convert celsius value to fahrenheit. 


c =int(input('Enter celcius: '))

f = c * 1.8 + 32


print('Fahrenheit is: ',f)


#Q3:- Take 2 numbers as input from the user.
# Write a program to swap the numbers without 
# using any special python syntax.


a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

temp = a
a = b
b = temp

print('Number after swap:a:',a,'b:',b,)


#Q5:- Write a program to find the simple interest when the value of principle,
# rate of interest and time period is provided by the user.

p =int(input('Enter principle amount: '))
r =int(input('Enter rate of percentage: '))
t =int(input('Enter time period: '))
d = 100
simple_interest = p*r*t/d


print('Simple Interest: ',simple_interest)

total_amount = p + simple_interest


print('Total amount: ',total_amount)


#Q6:- Write a program that will tell the number of dogs and 
#chicken are there when the user will provide the value of total heads and legs.


heads =int(input('Enter total heads: '))
legs =int(input('Enter total legs: '))

dogs =(legs - 2 * heads) // 2

chicken = heads - dogs


print('Number of chickens: ',chicken)
print('Number of Dogs: ',dogs)

#Q7:- Write a program to find the sum of squares of first n 
#natural numbers where n will be provided by the user.


n = int(input('Enter value of n : '))

sum_squares = 0

for i in range(1,n + 1):
    sum_squares += i * i
   


print('Sum of squares: ',sum_squares)   




