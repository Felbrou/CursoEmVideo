#Python Exercise 49: Redo CHALLENGE 9, showing the times tables of a number the user chooses, only now using a for loop.
f1 = int(input('Enter a number and discover your multiplication table: '))
print('-'*32)
print("\033[035mThe multiplication table of {} is:\033[m".format(f1))
print('-'*32)
for f2 in range (0,11):
    print("\033[032m{} x {}\033[m = \033[034m{}\033[m".format(f1,f2,f1 * f2))

