# Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma
# mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

vel = float(input('Qual a velocidade atual do carro?'))
if vel > 80:
    print('MULTADO! Você excedeu o limite permitido de 80km/h')
    multa = (vel-80)*7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))

print('Tenha um bom dia, dirija com segurança!')