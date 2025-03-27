texto = input("Informe um texto: ")

textoInverso = texto[::-1]

if texto == textoInverso:
    print(f"A palavra {texto} é um palíndromo.")
else:
    print(f"A palavra {texto} não é um polídromo.")