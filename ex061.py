# Python Exercise 61: Redo CHALLENGE 51, reading the first term and reason from an AP,
# showing the first 10 terms of the progression using the while structure.
a1 = int(input("Enter the first term [a1] of the A.P.: "))
r = int(input("Now the reason value: "))
n = 1
print("\033[34mThe reason term of number \033[33m{}\033[m:".format(a1))
while n < 11:
    a_n = a1 + (n - 1) * r
    print(' {}'.format(a_n), end='')
    print(' \033[31m->\033[m' if n <= 9 else '', end='')
    n += 1

