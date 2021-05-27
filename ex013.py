#   Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Saiba seu salário com o valor de 15% de acréscimo R$:'))
novo_salario = salario + (salario*15/100)
print('Seu salário de R${:.2f} com aumento de 15% ficará R${:.2f}'.format(salario, novo_salario))
