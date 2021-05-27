p_largura = float(input('Saiba a quantidade de tinta necessária para pintar a sua parede \nE economize! \nQual a largura da sua parede em metros? \nLargura:'))
p_altura = float(input('E a altura?'))
area_parede = p_largura * p_altura
area_pintada= (p_largura * p_altura) / 2
print('Sua parede tem a dimensão de {}x{}, e sua área {:.3f}m² \nE serão necessários {:.2f}l de tinta, para pintar sua parede!'.format(p_largura, p_altura, area_parede, area_pintada))