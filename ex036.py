#PROPERTY-FINANCING

valorcasa = float(input("Qual o valor do imóvel que você deseja financiar? R$"))
salario = float(input("Agora digite o valor do se salário: R$"))
anos = int(input("Em quantos anos deseja quitar o imóvel? "))
prestacao = valorcasa / (anos * 12)
minimo = salario * 0.3
print("Para pagar uma casa de R${:.2f} em {} anos.".format(valorcasa,anos))
print("A prestação será de R${:.2f}".format(prestacao))
if prestacao <= minimo:
    print("Financiamento pode ser \033[34mCONCEDIDO\033[m!")
else:
    print("Financiamento \033[33mNEGADO\033[m!")
