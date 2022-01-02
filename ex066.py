from time import sleep
print('SUM CALCULATOR')
print('~~'*8)
sum_of_numbers, n, cont = 0, 0, 0
sleep(1)
while True:
    print('Enter a value:')
    n = int(input("Press \033[31m999\033[m to quit: "))
    print('\033[32m---\033[m'*12)
    if n != 999:
        sum_of_numbers += n
        cont += 1
        sleep(1)
    else:
        break
print('\033[34mQuiting\033[m')
sleep(2)
print(f"You have enter \033[35m{cont}\033[m and the sum is \033[35m{sum_of_numbers}\033[m")
print('\033[32m---\033[m'*12)
print('END OF PROGRAM')