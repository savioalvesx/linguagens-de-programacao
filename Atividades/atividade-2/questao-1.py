print("Este programa verifica quem é maior entre dois números.\n")

numero1 = int(input("Informe o 1º número: "))
numero2 = int(input("Informe o 2º número: "))

if numero1 > numero2:
    print(f"O número maior é {numero1}")
elif numero1 == numero2:
    print("Os números são iguais.")
else:
    print(f"O número maior é {numero2}")
