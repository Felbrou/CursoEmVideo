m = float(input('DIga sua metragem:'))
dm = m * 10
cm = m * 100
mm = m * 1000
dam = m / 10
hec = m / 100
km = m / 1000
print('Esse valor em decímetro(dm) é {:.0f} \nO valor convertido em centímetros(cm) é de: {:.0f}'.format(dm,cm))
print('E em milímetros(mm) é de: {}.Logo {} em decamêtro(dam) é {} \nEm hectômetro é: {}\nEm quilômetro é {}'.format(mm, m, dam, hec, km))