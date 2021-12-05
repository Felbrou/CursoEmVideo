#Python Exercise 46: Make a program that shows on screen a countdown to the fireworks burst
from time import sleep
print("\033[035mFIREWORKS COUNTDOWN\033[m")
for c in range (10, -1,-1):
    sleep(1)
    print(c,'!!!')

sleep(2)
print("  \U0001F386  ","  \U0001F386  ","  \U0001F386  ")
print("\033[035m  HAPPY NEW YEAR!!!!\033[m")
print("  \U0001F387  ","  \U0001F387  ","  \U0001F387  ")