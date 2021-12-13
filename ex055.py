#Python Exercise 55: Write a program that reads the weight of five people.
#At the end, show which was the highest and lowest weight read.
higher = 0
lower = 0
for p in range(1,6):
    weight = float(input("Weight of {}ª person ".format(p)))
    if p == 1:
        higher = weight
        lower = weight
    else:
        if weight > higher:
            higher = weight
        if weight < lower:
            lower = weight
print("The greater weight read was {}kgs".format(higher))
print("And the lower weight read was {}kgs".format(lower))









