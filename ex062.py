# Python Exercise 62: Improve CHALLENGE 61 by asking the user if they want to show some more terms.
# The program will exit when it says it wants to show 0 terms.
a1 = int(input('Digit the first term: '))
reason = int(input('Now the reason of A.P. : '))
term = a1
count = 1
tot = 0
more = 10
while more != 0:
    tot = tot + more
    while count <= tot:
        print('{} ->'.format(term), end='')
        term += reason
        count += 1
    print('\033[31mPAUSE\033[m')
    more = int(input('How much more terms do you want to know? '))
print('END! Progression finalized with {} terms'.format(tot))


