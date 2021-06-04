#Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou
# não formar um triângulo.

print('-='*12)
print('ANALISADOR DE TRIÂNGULOS')
print('-='*12)


a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if (a + b < c) or (a + c < b) or (b + c < a):
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')
else:
    print('Os segmentos acima PODEM FORMAR um triâgulo')