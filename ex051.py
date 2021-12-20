#Python Exercise 51: Develop a program that reads the first term and reason of an AP. At the end,
#show the first 10 terms of this progression.
a_first = int(input('Digit the first term [a1]:')) #first term of sequence
r = int(input('Now the reason [r] of the arithmetic progression: '))#reason of A.P.
a_tenth = a_first + (10 - 1) * r

print('The Arithmetic Progression of \033[034m{}\033[m is:'.format(a_first))
print('\033[31m-\033[m'*34)
for var in range(a_first, a_tenth + r, r):
    print('\033[34m{}\033[m'.format(var), end=' \033[037m->\033[m')
print('\033[36mDONE!\033[m')


