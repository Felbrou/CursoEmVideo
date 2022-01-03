# Python Exercise 069: Create a program that reads the age and gender of various people.
# For each registered person, the program must ask whether the user wants to continue or not. At the end, show:
# A) how many people are over 18 years old.
# B) how many men were registered.
# C) how many women are under 20 years old.
from time import sleep

age_over_18, men_register, women_under = 0, 0, 0

while True:
    print('-' * 17)
    print(' \033[34mPEOPLE REGISTER\033[m')
    print('-' * 17)
    age = int(input("Age: "))
    gender = ' '
    while gender not in 'MF':
        gender = str(input("Gender: [M/F] ")).strip().upper()[0]
    if age > 18:
        age_over_18 += 1
    if gender == 'M':
        men_register += 1
    if gender == 'F' and age < 20:
        women_under += 1
    process = ' '
    while process not in 'YN':
        print('---' * 10)
        process = str(input("Want register more? [Y/N] ")).strip().upper()[0]
        print('---' * 10)
    if process == 'N':
        break
print('\033[31mQUITING\033[m')
sleep(2)
print('\033[33mEND OF REGISTRATION\033[m')
print(f'\033[34m1)\033[m \033[33m{age_over_18}\033[m people are over 18 years old.'
      f'\n\033[34m2)\033[m \033[33m{men_register}\033[m men were registered.'
      f'\n\033[34m3)\033[m \033[33m{women_under}\033[m women are under 20 years old.')