#Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.


import random
print('Vou pensar em número entre 0 e 5. Tente adivinhar')
n = int(input('Digite um número de 0 a 5: '))
x = random.randint(0,5)
print('PROCESSANDO...')
if n == x:
    print('PARABÉNS!!!Você conseguiu me vencer')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(x,n))