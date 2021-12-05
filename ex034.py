# Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

'''salario = float(input('Qual é o salário do funcionário? R$'))
if (salario > 1250):
    aumento = salario * 0.10 #10% é igual a 0.10, ou seja multipliquei o salário por 0.10

if (salario <= 1250):
    aumento = salario * 0.15 #15% é igual a 0.15, ou seja multipliquei o salário por 0.15

print('Seu aumento é de R${:.2f}, o que dá um salário total de R${:.2f}'.format(aumento,(salario + aumento)))'''


#Outra forma

salario = float(input('Qual o salário do funcionário? R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    salario > 1250
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(salario,novo))
