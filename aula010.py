# Condições em Python

#1a Estrutura
#tempo = int(input('Quantos anos tem eu carro?'))
#if tempo<=3:
#    print('Carro novo!Parabéns!')
#else:
#    print('Carro velho :c')
#print('--FIM--')

#2a Estrutura
#tempo = int(input('Qantos anos tem seu carro?'))
#print('Carro novo' if tempo<=3 else 'Carro velho:c')
#print('--FIM--')

#Exemplo aula
#nome = str(input('Qual é o seu nome?'))
#if nome == 'Felipe':
#    print('Você sabia? Felipe vem prenome grego Φίλιππος [Fílipos], latinizado em Philippus, composto de φιλέω [filéo], "querer, amar com afeto de amizade", e ἵππος [híppos], "cavalo". Na Grécia antiga, a propriedade de cavalos era disponível somente a pessoas ricas o bastante para pagá-los.')
#if nome == 'Matheus':
#    print('Voce Sabia? Mateus é um nome de idioma português. É derivado do nome hebraico "מתתיהו"(Matityahu), que significa "Presente de Javé". Há também a variante em português Matheus.')
#print('Bom dia {}!'.format(nome))

#Exemplo 2 aula
n1 = float(input('Digite sua primeira nota:'))
n2 = float(input('Digite sua segunda nota:'))
m = (n1 + n2)/ 2
print('A sua média é {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim. ESTUDE MAIS!')

