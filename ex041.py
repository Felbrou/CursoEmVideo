#RANKING-ATHLETES
#The National Swimming Confederation
#Needs a program that reads an athlete's year of birth and shows their category, according to age:
#Up to 9 years old: KINDERGARTEN
#Up to 14 years old: CHILDREN
#Up to 19 years old: JUNIOR
#Up to 25 years old: SENIOR
#Over 25 years old: MASTER
from datetime import date
birth = int(input("\033[034mWhat's your year of birth?\033[m "))
actualdate = date.today().year
age = actualdate - birth

if age <= 9:
    print("You have \033[034m{}\033[m years, your category is \033[034mKINDERGARTEN\033[m.".format(age))
elif age > 9 and age <= 14:
    print("You have \033[034m{}\033[m years, your category is \033[034mCHILDREN\033[m.".format(age))
elif age > 14 and age <= 19:
    print("You have \033[034m{}\033[m years, your category is \033[034mJUNIOR\033[m.".format(age))
elif age > 19 and age <= 25:
    print("You have \033[034m{}\033[m years, your category is \033[034mSENIOR\033[m.".format(age))
elif age > 25:
    print("You have \033[034m{}\033[m years, your category is \033[034mMASTER\033[m".format(age))


