#COMPARING-NUMBERS

n1 = int(input('Enter a number:'))
n2 = int(input('Enter another number:'))

if n1 > n2:
    print('The first number \033[034m{}\033[m is greater than the second number \033[033m{}\033[m.'.format(n1,n2))
elif n2 > n1:
    print('The second number \033[034m{}\033[m is greater than the first number \033[033m{}\033[m.'.format(n2,n1))
else:
    print('The first number \033[034m{}\033[m and the second number \033[034m{}\033[m are equal.'.format(n1,n2))