print('Enter two numbers to perform operation:\n')

a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

#Arithmatic Operators

print('\nArithmetic Operators: ')

print('Sum: ',a + b)
print('Difference: ',a - b)
print('Product : ',a * b)
print('Division: ',a / b)
print('Floor Division: ',a // b)
print('Modulus: ',a % b)
print('Exponentiation: ',a ** b)

#Relational Operators

print('\nRelational Operators')

print('a > b: ',a > b)
print('a < b: ',a < b)
print('a >= b: ',a >= b)
print('a <= b:',a <= b)
print('a == b: ',a == b)
print('a != b: ',a != b)

#logical opertors 

print('\nLogical Operator: ')


print('a and b: ',a and b)
print('a or b: ',a or b)
print('not a: ',not a)

#Bitwise Operators

print('\nBitwise Operators')
print('a & b: ',a & b )
print('a | b: ',a | b)
print('a ^ b: ',a ^ b)
print('~a: ',~a)
print('a >> b: ',a >> b)
print('a << b: ',a << b)
      
print('\nAssignment Operators: ')

# x is used to keep the original value of a unchanged

x = a
x += b
print('x+=b: ',x)
x-=b
print('x-=b: ',x)
x*=b
print('x*=b: ',x)
x/=b
print('x/=b: ',x)
x//=b
print('x//=b: ',x)
x**=b
print('x**=b: ',x)


#Membership Operator

#in / not in
print('\nMembership Operator: ')
print('D' in 'Delhi')
print('D' not in 'Delhi')
