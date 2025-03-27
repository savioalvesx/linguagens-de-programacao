print("Este programa imprime a tabuada de acrodo o número.\n")

numero = int(input("Informe um número: "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} X {i} = {resultado}")  #print(f"{numero} X {i} = {numero*i}") Sem variavel resultado.