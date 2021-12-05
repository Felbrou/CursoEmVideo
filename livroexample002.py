#LOGIC-TEST-OR

sexo = str(input("Qual o sexo? \nM(masculino) ou F (feminino): "))
sexo = sexo.upper() or sexo.lower()

if (sexo == "F") or (sexo == "M"):
    print("Sexo válido")
elif sexo == "MASCULINO" or sexo == "FEMININO":
    print("Sexo válido")
else:
    print("Sexo inválido")