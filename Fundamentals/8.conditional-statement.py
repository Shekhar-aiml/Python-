#if-else 

age =int(input('Enter the age for Driving License: '))

if age >= 18:
    print('You are eligible') 
else:
    print('You are not eligible ')    

#elif 
email = input('Enter Your Email: ')
password = input('Enter Your Password: ')

if email == 'example@gmail.com' and password == '1221':
    print('Login successfull')
elif email == 'example@gmail.com' and password != '1221':
    print('Incorrect Password Try Again!! ') 
    password = input('Enter password again: ')
    if password == '1221':
     print('Login Succcesfull') 
    else:
     print('Incorrect password Try again after some time!: ')

else:
 print('Login Failed!!')    

#Menu driven atm task 

menu = int(input("""
Hi how can i help you!!
1.Change pin                
2.Check balance
3.Withdraw:\n """))

if menu == 1:
    print('Change the pin: ')
elif menu == 2:
    print('Show Balance: ')
elif menu == 3:
    print('Withdraw')   
else:
    print('You Entered Wrong Number!!') 

#Q find the min of 3 number 

a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
c = int(input('Enter third number: '))

if a<b and a<c:
    print('smallest is: ',a)
elif b<c:
    print('smallest is:',b)
else:
    print('smallest is: ',c) 
