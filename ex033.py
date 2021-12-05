# Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.


from time import sleep

primeiro = int(input('Digite o primeiro valor:'))
segundo = int(input('Digite o segundo valor:'))
terceiro = int(input('Digite o terceiro e último valor:'))

# Verificando qual o maior valor
maior = primeiro

if (segundo > maior):
    maior = segundo
if (terceiro > maior):
    maior = terceiro

print('O número maior é ',maior)

# Verificando qual o menor valor
menor = primeiro

if (segundo < menor):
    menor = segundo
if (terceiro < menor):
    menor = terceiro

print('O número menor é ', menor)

# Outra forma

'''a = int(input('Primeiro valor:'))
b = int(input('Segundo valor:'))
c = int(input('Terceiro valor:'))
#Verificando o menor
menor = a
if (b < a) and (b < c):
    menor = b
if (c < a) and (c < b):
    menor = c
#Verificando o maior
maior = a
if (b > a) and (b > c):
    maior = b
if (c > a) and (c > b):
    maior = c
print('O menor valor é {} e maior valor é {}'.format(menor,maior))'''
