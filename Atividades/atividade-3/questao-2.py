print("Este programa imprime a tabuada de acordo com o número.\n")

numeros = list(range(1, 10))

numero = int(input("Informe um número: "))

for i in numeros:
    print(f"{numero} X {i} = {numero*i}") 