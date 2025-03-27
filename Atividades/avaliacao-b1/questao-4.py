numeroPositivo = 0
numeroNegativo = 0
for i in range(1,11): # Ou for i in range(10)
    numero = int(input(f"Informe o {i}º número: "))

    if numero > 0:
        numeroPositivo = numeroPositivo + 1 # numeroPositivo += 1
    else:
        numeroNegativo = numeroNegativo + 1 # numeroNegativo += 1

print(f"A quantidade de números negativos é {numeroNegativo}.")
print(f"A quantidade de números positivos é {numeroPositivo}.")