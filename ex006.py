n1 = int(input('Escolha um número e descubra o seu dobro, triplo e raiz quadrada:'))
dob = n1 * 2
tri = n1 * 3
rz = n1 ** (1/2)
print('O dobro de {} é, {} e o seu triplo é {}.'.format(n1,dob,tri))
print('E por fim sua raiz é, {:.3f}'.format(rz))