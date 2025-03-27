print("Este programa verifica se o valor é positivo ou negativo.\n")
      
valor = int(input("Informe um valor: "))

if valor > 0:
    print(f"O valor informado {valor} é positivo.")
elif valor == 0:
    print("0 é número neutro. Informe um número positivo ou negativo.")
else:
    print(f"O valor informado {valor} é negativo.")