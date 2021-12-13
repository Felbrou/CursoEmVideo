#Python Exercise 56: Develop a program that reads the name, age, and gender of 4 people.
#At the end of the program, show: the average age of the group, what the oldest man's name is,
# and how many women are under 20 years old.
sum_age = 0
average_age = 0
higher_age_m = 0
older_name = ''
tot_wom_20 = 0
for p in range(1, 5):
    print("\033[32m====  {}ª person ====\033[m".format(p))
    name = str(input("What it's {}º name? ".format(p))).strip()
    age = int(input("Enter your age: "))
    gender = str(input("Now your gender(Type [M] or [F]): ")).strip()
    sum_age += age
    if p == 1 and gender in 'Mm':
        higher_age_m = age
        older_name = name
    if gender in 'Mm' and age > higher_age_m:
        higher_age_m = age
        older_name = name
    if gender in 'Ff' and age < 20:
        tot_wom_20 += 1
average_age = sum_age / 4
print("The average age of the group is \033[33m{}\033[m.".format(average_age))
print("The older man in group is \033[36m{}\033[m, with \033[36m{}\033[m years old.".format(older_name, higher_age_m))
print("The total of women under \033[35m20 years\033[m is \033[35m{}\033[m.".format(tot_wom_20))


