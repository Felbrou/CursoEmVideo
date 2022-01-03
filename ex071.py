# Python Exercise 071: Create a program that simulates the operation of an ATM.
# At the beginning, ask the user what will be the amount to be withdrawn (integer)
# And the program will inform how many bills of each amount will be delivered.
# NOTE: consider that the cashier has bills of U$50, U$20, U$10 and U$1.
print('='*30)
print('{:^38}'.format('\033[34mPython Course ATM\033[m'))
print('='*30)
print('How much do you want withdrawn?')
print('\033[33mMinimum withdrawn U$50\033[m')
print('---'*10)
value = int((input('Enter value U$>>> ')))
total = value
bill = 50
total_bills = 0
while True:
    if total >= bill:
        total -= bill
        total_bills += 1
    else:
        if total_bills > 0:
            print(f'Total de {total_bills} dollar bills of U${bill} ')
        if bill == 50:
            bill = 20
        elif bill == 20:
            bill = 10
        elif bill == 10:
            bill = 1
        total_bills = 0
        if total == 0:
            break


print('THANK YOU! HAVE A NICE DAY')


