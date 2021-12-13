#Python Exercise 52: Write a program that reads an integer and tells you whether or not it is a prime number.
n = int(input('Enter a number and find out if it is prime or not: '))
for n in range(2,n+1):
    for x in range(2,n):
        if n % x == 0:
            print ('\033[037m{}\033[m is equal {}x{}'.format(n,x,n//x))
            break
    else:
        print('-'*22)
        print('\033[036m{}\033[m \033[033mis a prime number!\033[m'.format(n))
        print('-' * 22)
