print("Este programa verifica se um número é par ou ímpar.\n")

numero = int(input("Informe um número: "))

if numero % 2 == 1:
    print(f"O número {numero} é impar")
else:
    print(f"O número {numero} é par")