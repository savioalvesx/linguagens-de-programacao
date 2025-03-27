print("Este programa cria um lista de 5 número e remove de acordo com o usúario.\n")

numeros = []

for i in range(5):
    numero = int(input(f"Informe {i+1}º número: "))
    numeros.append(numero)

print("\nLista atual:", numeros)

remover = int(input("Informe um número que deseja remover: "))

if remover in numeros:
    numeros.remove(remover)
    print("\nNúmero removido!")

print("Lista atualizada:", numeros)
