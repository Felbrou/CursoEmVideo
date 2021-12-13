num = int(input('Digite um número e saiba se ele é primo: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('E por isso ele \033[32mÉ PRIMO\033[m')
else:
    print('E por isso ele \033[31mNÃO É PRIMO\033[m')