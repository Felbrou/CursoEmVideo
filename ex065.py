n, tot, count, ave, greater, lower = 0, 0, 0, 0, 0, 0
s = ''
while s != 'N':
    n = int(input('enter a number: '))
    s = str(input('Wish continue [Y/N]? ')).upper().strip()[0]
    if n != 0:
        count += 1
        tot += n
        ave = tot/count
    if count == 1:
        greater = n
        lower = n
    if count > 1:
        if n > greater:
            greater = n
        elif lower > n:
            lower = n

print('You enter {} numbers and the average of them is {:.2f}'.format(count, ave))
print('And the greater value is \033[35m{}\033[m ...and the lower \033[33m{}\033[m'.format(greater, lower))
