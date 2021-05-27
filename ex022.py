nome = input('Qual seu nome?')
print('Seu nome com letra maiúscula é:',nome.upper())
print('Seu nome com letras minúsculas é:', nome.lower())
dividido = nome.split()
nomejunto = ''.join(dividido)
print('Seu nome tem o total de:', len(nomejunto))
print('E seu primeiro nome {} tem '.format(dividido[0]), len(dividido[0]))

