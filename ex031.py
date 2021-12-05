#Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

kilometros = float(input('Digite a distância de sua viagem:'))
if kilometros <= 200:
   preço = kilometros * 0.50
else:
    preço = kilometros * 0.45
print('O preço da passagem sairá no valor de R${:.2f}'.format(preço))


#Versão simplificada

'''kilometros = float(input('Digite a distância de sua viagem:'))
preço = kilometros * 0.50 if kilometros <= 200 else kilometros * 0.45
print('O preço da passagem sairá no valor de R${:.2f}'.format(preço))'''


