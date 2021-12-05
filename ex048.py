#Python Exercise 48: Write a program that calculates the sum of all numbers that are multiples of three and it is
# in the range 1 to 500.

sum = 0 #sum counter
count = 0 #counter
for n in range(1,501): #number 1 up to 500
    if n % 2 != 0: #discover if n is odd
        if n % 3 == 0: # multiples of 3
            count += 1 #count will receive 1 in each loop
            sum += n #sum = sum + n
print("The sum of the \033[034m{}\033[m solicited values is \033[034m{}\033[m".format(count,sum))





