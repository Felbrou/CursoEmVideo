#Exercício Python 30: Crie um programa que leia um número inteiro
# e mostre na tela se ele é PAR ou ÍMPAR.

print('==--'*13)
print(' DIGITE UM NÚMERO E VOU DIZER SE ELE É PAR OU ÍMPAR')
print('==--'*13)
numero = int(input('Digite um número:'))
if (numero % 2) == 0:
    print('O número {} é PAR'.format(numero))
else:
    print('O número {} é ÍMPAR'.format(numero))