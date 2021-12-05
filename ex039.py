#MILITARY-DRAFT
from datetime import date

actualyear = date.today().year
birth = int(input('What year you were born? '))
age = actualyear - birth

if age > 18:
    agegreater = (age - 18)
    print("You have \033[034m{}\033[m years."
          "You should have joined the army in {}. \033[034m{}\033[m year(s) have passed. ".format(age,(birth + 18),agegreater))
elif age == 18:
    print('You were birth in \033[034m{}\033[m, '
          '\nand have \033[034m18\033[m year(s), look for a nearest army post to enlist!'.format(birth))
else:
    agelower = (age - 18) * -1
    print("You have \033[034m{}\033[m years. You don't have the age required to join the army yet."
          "\nIn \033[034m{}\033[m years ({}) you can enlist in the army.".format(age,agelower,(birth + 18)))
