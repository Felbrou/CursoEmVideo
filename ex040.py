#GRADE-AVERAGE-PROGRAM
#Create a program that reads two grades from a student and calculates their average,
#showing a message at the end, according to the average achieved:
#Average below 5.0: FAILED
#Average between 5.0 and 6.9: RECOVERY
#Average 7.0 or above: PASSED

grade1 = float(input("What´s the first grade? "))
grade2 = float(input("Now, the second: "))
average = (grade1 + grade2) / 2

if average >= 7.0:
    print("\033[034mCONGRATULATIONS\033[m, your average grade is \033[034m{:.1f}\033[m, you were approved!".format(average))
elif (average >= 5.0) and (average <= 6.9):
    print("Your average grade is \033[033m{:.1f}\033[m, you have to go summer school.".format(average))
elif average <= 4.9:
    print("Your grade is \033[031m{:.1f}\033[m, you are \033[031mREPROVED\033[m!".format(average))