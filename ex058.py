# Python Exercise 058: Improve the CHALLENGE 028 game where the computer will "think" of a number between 0 and 10.
# But now the player will try to guess until he sets the right number.
# Showing at the end how many attempts were needed to win.
from time import sleep
import random

count = 0
print('\033[35m-=-' * 15)
print('  TRY TO GUESS WHAT NUMBER I WILL CHOICE!!!')
print('-=-' * 15, '\033[m')
n = int
x = random.randint(0, 10)
while n != x:
    n = int(input('Enter another number: '))
    x = random.randint(0, 10)
    print('\033[36mLOADING...\033[m')
    sleep(2)
    print("\033[31mYOU LOOSE\033[m...I choose \033[33m{}\033[m and you \033[32m{}\033[m... TRY AGAIN.".format(x, n))
    count += 1
if n == x:
    print('  \U0001F386  \033[35mCONGRATULATIONS!!!\033[m  \U0001F386  ')
    print('YOU WIN!!! I choose {} and you too!You have won in {} rounds'.format(n, count))


