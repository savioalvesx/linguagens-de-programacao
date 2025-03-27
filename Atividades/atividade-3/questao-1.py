print("Este programa ler 5 números e mostra o maior, menor e soma total.\n")

numeros = []

for i in range(5):
    numero = int(input(f"Informe o {i+1}º número: "))
    numeros.append(numero)

maior_numero = max(numeros)
menor_numero = min(numeros)
soma_total = sum(numeros)

print(f"\nMaior número: {maior_numero}")
print(f"Menor número: {menor_numero}")
print(f"A soma de todos os números: {soma_total}")