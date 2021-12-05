#Python Exercise 50: Develop a program that reads six integer numbers and shows the sum of only those that are even.
#If the value entered is odd, disregard it.
sum = 0
for c in range (1, 7):
    n = int(input('Enter the {}º value and know the sum off the even numbers: '.format(c)))
    if n % 2 == 0:
        sum += n
print("\033[036mThe sum of all even numbers is \033[33m{}\033[m".format(sum))
