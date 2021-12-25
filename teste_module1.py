lower, greater = 0, 0
n = 0
while n != 999:
    n = int(input('valor'))
    if n > greater:
        greater = n
    elif lower < n < lower:
        lower = n

    print('greater {}...lower {}'.format(greater, lower))