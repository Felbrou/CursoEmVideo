# Python Exercise 068: Develop a program that plays even or odd with the computer...
# The game will only be stopped when the player loses...
# Show the total consecutive victories he has won at the end of the game.
from random import randint
from time import sleep
pj = 0
print("LET'S PLAY \033[33mEVEN\033[m OR \033[35mODD\033[m")
print('---'*10)
sleep(1)
while True:
    player_number = int(input("Digit a number: "))
    cpu = randint(0, 100)
    sum_number = cpu + player_number
    player_choice = ' '
    while player_choice not in 'EO':
        player_choice = str(input("\033[33mEVEN\033[m or \033[35mODD\033[m [E/O]>>> ")).strip().upper()[0]
    sleep(1)
    print(f"You have input \033[34m{player_number}\033[m and the computer \033[34m{cpu}\033[m."
          f"The total is \033[36m{sum_number}\033[m ")
    sleep(1)
    if sum_number % 2 == 0:
        print('Its \033[33mEVEN!\033[m')
        if player_choice == 'E':
            pj += 1
            print("\033[32mYou Win!\033[m")
            print('---' * 10)
            print("Let's play again...")
        else:
            break
    if sum_number % 2 != 0:
        print('Its \033[35mODD!\033[m')
        if player_choice == 'O':
            pj += 1
            print("\033[32mYou Win!\033[m")
            print('---' * 10)
            print("Let's play again...")
        else:
            break
print('---' * 13)
print(f'You Loose! You have win \033[32m{pj}\033[m times')
print('\033[31mGame Over\033[m')
print('END OF PROGRAM')
