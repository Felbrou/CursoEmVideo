# Python Exercise 060: Write a program that reads any number and displays its factorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
n = int(input('Enter a number and discover the factorial of it: '))
c = n
f = 1
print('\033[33mCalculing {}!\033[m: '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1

print('\033[35m{}\033[m'.format(f))