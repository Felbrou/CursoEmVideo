from time import sleep
print('   Welcome to \033[036mJAN-KEN-PON(JOKENPÔ)\033[m\n     \033[032mCreated by Felipe Verissimo\033[m')
print(39*'¨')
print("  \033[032mWHO DO 3 POINTS FIRST WIN THE GAME\033[m")
print(39*'-')
pj=0
pc=0

while (pj<3 and pc<3):
    from random import randint
    print('Player=%d' % pj)
    print('PC=%d' % pc)

    player = int(input("Choose: [0] Stone [1] Paper [2] Scissor\n\033[031mPlay against me!!! \033[m"))
    print('JO...')
    sleep(1)
    print('KEN...')
    sleep(1)
    print('PO!!!')
    items = ('Stone','Paper','Scissor')
    cpu=randint(0,2)
    if (player == 0):
        if (cpu == 0):
            print('-='*11)
            print('PC choose \033[1;91m{}\033[m'.format(items[cpu]))
            print('You choose \033[1;34m{}\033[m'.format(items[player]))
            print("\033[032mDRAW\033[m")
            print('-=' * 11)
        elif (cpu == 1):
            print('-=' * 11)
            print('PC choose \033[1;91m{}\033[m'.format(items[cpu]))
            print('You choose \033[1;34m{}\033[m'.format(items[player]))
            print("\033[036mYOU LOOSE!\033[m")
            print('-=' * 11)
            pc+=1
        elif (cpu == 2):
            print('-=' * 11)
            print('PC choose \033[1;91m{}\033[m'.format(items[cpu]))
            print('You choose \033[1;34m{}\033[m'.format(items[player]))
            print("\033[032mYOU WIN!\033[m")
            print('-=' * 11)
            pj+=1
    elif (player == 1):
        if (cpu == 1):
            print('-=' * 11)
            print('PC choose \033[1;91m{}\033[m'.format(items[cpu]))
            print('You choose \033[1;34m{}\033[m'.format(items[player]))
            print("\033[032mDRAW\033[m")
            print('-=' * 11)
        elif (cpu == 0):
            print('-=' * 11)
            print('PC choose \033[1;91m{}\033[m'.format(items[cpu]))
            print('You choose \033[1;34m{}\033[m'.format(items[player]))
            print("\033[032mYOU WIN!\033[m")
            print('-=' * 11)
            pj+=1
        elif (cpu == 2):
            print('-=' * 11)
            print('PC choose \033[1;91m{}\033[m'.format(items[cpu]))
            print('You choose \033[1;34m{}\033[m'.format(items[player]))
            print("\033[036mYOU LOOSE!\033[m")
            print('-=' * 11)
            pc+=1
    elif (player == 2):
        if (cpu == 2):
            print('-=' * 11)
            print('PC choose \033[1;91m{}\033[m'.format(items[cpu]))
            print('You choose \033[1;34m{}\033[m'.format(items[player]))
            print("\033[032mDRAW\033[m")
            print('-=' * 11)
        if (cpu == 0):
            print('-=' * 11)
            print('PC choose \033[1;91m{}\033[m'.format(items[cpu]))
            print('You choose \033[1;34m{}\033[m'.format(items[player]))
            print("\033[036mYOU LOOSE!\033[m")
            print('-=' * 11)
            pc+=1
        elif (cpu == 1):
            print('-=' * 11)
            print('PC choose \033[1;91m{}\033[m'.format(items[cpu]))
            print('You choose \033[1;34m{}\033[m'.format(items[player]))
            print("\033[032mYOU WIN!\033[m")
            print('-=' * 11)
            pj+=1
if (pj == 3):
    print('=' * 33)
    print("\033[034mCONGRATULATIONS, YOU WON THE GAME!!!\033[m")
    print('=' * 33)

elif (pc == 3):
    print('=' * 33)
    print("\033[031mYOU LOOSE THE GAME, TRY AGAIN!\033[m")
    print('=' * 33)
