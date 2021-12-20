#PythonExercice57...Write a program tha reads the gender of a person, but only accepts 'M' and 'F' values
#If enter a wrong value ask to type again the right value
from time import sleep
gender = ''

while gender != '0':
    print('\033[37m====What is your gender====\033[m')
    print('Type "0" to quit program.')
    gender = str(input('Type [F/M] ')).upper().strip()[0]
    if gender == 'M':
        print('Gender \033[36mmasculine\033[m [{}] registred!'.format(gender))
    elif gender == 'F':
        print('Gender \033[35mfeminine\033[m [{}] registred! '.format(gender))
    elif gender == '0':
        print('\033[31mQuiting...\033[m')
        sleep(2)
    else:
        print('\033[31mWrong value!\033[m please write \033[33m[M]\033[m for masculine or \033[33m[F]\033[m \n'
              'for feminine gender.')

print('\033[34m====END OF PROGRAM====\033[m')