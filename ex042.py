#ANALYSING-TRIANGLES
#Develop a program that reads the length of three lines and tells the user if they can or
#does not form a triangle.

print('\033[036m-=\033[m'*12)
print("  TRIANGLE'S ANALYSER")
print('\033[036m-=\033[m'*12)

ab = float(input("\033[035mWhat's the triangle's length side AB?\033[m "))
bc = float(input("\033[036mWhat's the triangle's length side BC?\033[m "))
ac = float(input("\033[033mWhat's the triangle's length side AC?\033[m "))

if (ab + bc < ac) or (ab + ac < bc) or (ac + bc < ab):
    print("\033[031mERROR!\033[mThese measurements cannot form a triangle.")
elif ab != bc and ab != ac and bc != ac:
    print("These measurements can form a \033[034mSCALENE TRIANGLE\033[m.")
elif ab == ac and ab != bc and ac != bc:
    print("These measurements can form a \033[034mISOSCELES TRIANGLE\033[m.")
elif ab == bc == ac:
    print("These measurements can form a \033[034mEQUILATERAL TRIANGLE\033[m.")