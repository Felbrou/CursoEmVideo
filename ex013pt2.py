preço = float(input('Digite o preço do produto que você quer calcular R$:'))
desconto = float(input('Digite o desconto:'))
novo_preço = preço - (preço * desconto / 100)
print('O preço com desconto é R$ {:.2f}'.format(novo_preço))