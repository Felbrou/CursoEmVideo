#Python Exercise 059: Create a program that reads two values and displays a menu on the screen:
#[ 1 ] sum
#[ 2 ] multiply
#[ 3 ] which is greater
#[ 4 ] other numbers
#[ 5 ] exit the program
#Your program must perform the requested operation in each case.
from time import sleep
c = 0
s = 0
m = 0
print("VERISSIMO'S CALCULATOR")
print('\033[37m---\033[m'*8)
while c != 5:
    x = int(input('Enter first value: '))
    y = int(input('Now, the second value: '))
    sleep(1)
    print('[ 1 ] Sum\n[ 2 ] Multiplication\n[ 3 ] Which number is greater\n[ 4 ] Choose other numbers\n[ 5 ] Exit')
    c = int(input('What operation do you want to do? '))
    if c == 1:
        s = x + y
        print('\033[33mCALCULATING...\033[m')
        sleep(1)
        print('\033[34m---\033[m' * 15)
        print('The sum of \033[32m{} + {}\033[m is \033[32m{}\033[m'.format(x, y, s))
        print('\033[34m---\033[m'*15)
    if c == 2:
        m = x * y
        print('\033[33mCALCULATING...\033[m')
        sleep(1)
        print('\033[34m---\033[m' * 15)
        print('The product multiplication of \033[32m{} x {}\033[m is \033[32m{}\033[m'.format(x, y, m))
        print('\033[34m---\033[m' * 15)
    if c == 3:
        print('\033[33mCALCULATING...\033[m')
        sleep(1)
        print('\033[34m---\033[m' * 15)
        if x > y:
            print('The number \033[32m{}\033[m is greater than \033[32m{}\033[m'.format(x, y))
        else:
            print('The number {} is greater than {}.'.format(y, x))
        print('\033[34m---\033[m' * 15)
    if c == 4:
        pass
    if c > 5:
        print('\033[31mInvalid Option! Try again\033[m')
print('\033[33mCLOSING THE PROGRAM...\033[m')
sleep(2)
print('THANK YOU FOR USING!')


