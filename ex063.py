# Python Exercise 63:
# Write a program that reads any integer N and displays the first N elements of a Fibonacci Sequence on screen.
# Example: 0 - 1 - 1 - 2 - 3 - 5 - 8
print(" \033[32mFibonacci's Converter\033[m")
print('---'*8)
term = int(input("Digit Fibonacci's term value up to..."))
a, b = 0, 1
tot = 0
print("The fibonacci sequence up to \033[36m{}\033[m its :".format(term))
while tot < term:
    print(a, end=' ')
    print(' -- ' if a != term else ' ', end='')
    a, b = b, a+b
    tot = tot + 1
print('\033[32mEND\033[m')





