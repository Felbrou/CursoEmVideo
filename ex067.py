# Python_Exercise_067 Develop a program that shows the multiplication table of each input number, one of each time.
# The program will be closed when the input number is negative
from time import sleep
n: int = 0

print('\033[35mMULTIPLICATION TABLE\033[m')
while True:
    n = int(input('Enter a number and know your multiplication table: '))
    print('\033[33mFor negative number the program will be closed\033[m')
    if n >= 0:
        print(f"The multiple table of {n} is:")
        for c in range(1, 11):
            print(f"{n} x {c} = {n*c}")
    else:
        break

print('\033[31mInvalid Value\033[m')
print('---'*6)
sleep(1)
print('Closing the Program')
print('---'*6)
sleep(2)
print('END OF PROGRAM')