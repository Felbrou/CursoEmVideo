#Python Exercise 54: Create a program that reads the birth year of seven people.
# At the end, show how many people aren't yet in majority age and how many are.

from datetime import date
actual_year = date.today().year
majority = 0
under_age = 0
for var in range(1,8):
    birth = int(input(f'Enter {var}º birth year: '))
    age = actual_year - birth
    if age >= 18:
        print('You \033[36m{}\033[m years old. You are in the majority age.'.format(age))
        majority += 1
    else:
        print("You have \033[36m{}\033[m years old. You are under age.".format(age))
        under_age += 1

print("\033[34m{}\033[m people(s) is in majority, and \033[34m{}\033[m is under age".format(majority,under_age))

