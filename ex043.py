#BODY-MASS-INDEX
"""Python Exercise 43: Develop logic that reads a person's weight and height, calculates their Body Mass Index (BMI),
and displays their status, according to the table below:
-BMI below 18.5: Underweight
-Between 18.5 and 25: Ideal Weight
-25 to 30: Overweight
-30 to 40: Obesity
-Over 40: Morbid Obesity"""
weight = float(input("What's your weight(kg)? "))
height = float(input("What's your height(m)? "))
bmi = weight / (height ** 2)

if bmi <= 18.5:
    print("Your BMI is \033[031m{:.1f}kg\033[m, you are \033[031mUNDERWEIGHT\033[m".format(bmi))
elif 18.5 <= bmi < 25:
    print("Your BMI is \033[032m{:.1f}kg\033[m, you are in the \033[032mIDEAL\033[m weight".format(bmi))
elif 25 <= bmi < 30:
    print("Your BMI is \033[033m{:.1f}kg\033[m, you are \033[033mOVERWEIGHT\033[m".format(bmi))
elif 30 <= bmi < 40:
    print("Your BMI is \033[033m{:.1f}kg\033[m, you are with \033[033mOBESITY\033[m".format(bmi))
elif bmi > 40:
    print("Your BMI is \033[031m{:.1f}kg\033[m, you are with \033[031mMORBID OBESITY\033[m".format(bmi))





