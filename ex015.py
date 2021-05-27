dias = int(input('Quantos dias alugados?'))
kms = float(input('Quantos quilômetros rodados?'))
valor = (dias * 60) + (0.15 * kms)
print('O valor a ser pago por {} dias e {:.3f}Kms rodados será de R${:.2f}'.format(dias,kms,valor))