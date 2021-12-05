#Python Exercise 49: Redo CHALLENGE 9, showing the times tables of a number the user chooses, only now using a for loop.
f1 = int(input('Enter a number and discover your multiplication table: ')) #first catch the first factor
print('-'*32)
print("\033[035mThe multiplication table of {} is:\033[m".format(f1))#showing the multiplication table of factor one
print('-'*32)
for f2 in range (0,11): #a loop for factor 2
    print("\033[032m{} x {}\033[m = \033[034m{}\033[m".format(f1,f2,f1 * f2))#here the output of the multiplication table

