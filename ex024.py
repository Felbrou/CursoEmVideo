#   Exercício Python 024 - Verificando as primeiras letras de um texto
#   Faça um programa que leia o nome de uma cidade
#   e diga se ela começa ou não com o nome "Santos".

cidade = str(input('Informe o nome da sua cidade:')).strip()
print(cidade[:5].upper() == 'SANTO')