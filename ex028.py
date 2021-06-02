#Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.


import random
from time import sleep
print ('**--**' * 9)
print ('  VOU PENSAR EM UM NÚMERO ENTRE 0 A 5, TENTE ADIVINHAR!')
print ('**--**' * 9)
n = int(input('Digite um número de 0 a 5: ')) #jogador tenta adivinhar
x = random.randint(0,5) #computador escolhe um número em cache
print('PROCESSANDO...')
sleep(3)
if n == x:
    print('PARABÉNS!!!Você conseguiu me vencer')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(x,n))