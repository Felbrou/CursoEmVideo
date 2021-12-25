sum = 0
while True:
    cont = int(input('Digite um numero'))
    if cont == 999:
        break
    print(cont, '-> ', end=' ')
    cont += 1
print('Acabou!')
