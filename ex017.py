import math
cop = float(input('Digite o comprimento do cateto oposto:'))
cadj = float(input('Agora o cateto adjacente:'))
hip = math.hypot(cop, cadj)
print('O comprimento da hipoteusa é: {:.2f}' .format(hip))