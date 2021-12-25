# Python Exercise 64: Develop a program that reads multiple integers numbers from the keyboard.
# The program will only stop when the user enters the value 999, which is the stopping condition.
# At the end, show how many numbers were entered and what was the sum between them (disregarding the flag).

print('\033[34mSUM CALCULATOR\033[m')
print('~'*14)
number = count = tot = 0

while number != 999:
    number = int(input('Enter a integer value\n\033[31m(OR TYPE 999 to exit)\033[m: '))
    if number != 999:
        tot += number
        count += 1
print('You have entered {} numbers and the sum of them is {}.'.format(count, tot))


