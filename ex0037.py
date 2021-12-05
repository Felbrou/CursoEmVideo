#NUMBER-BASE-CONVERTER

x = int(input("CONVERSOR DE BASES NUMÉRICAS\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\nDigite um número que queira converter: "))
base = int(input("Digite [1] para converter para binário.\nDigite [2] para octal.\nDigite [3] para hexadecimal:"))

if base == 1:
    conversao = bin(x)[2:] #[2:] for slicing method

elif base == 2:
    conversao = oct(x)[2:]

elif base == 3:
    conversao = hex(x)[2:]

else:
    ("Opção inválida, tente novamente.")

print("O número {} convertido para base {} é {}".format(x,base,conversao))






