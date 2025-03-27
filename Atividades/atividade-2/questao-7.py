import random

print("Este programa verifica se o numero informado bate com o numero gerado.\n")

numeroAleatorio = random.randint(0,10)

numero = int(input("Informe um número de 0 a 10: "))

if numeroAleatorio == numero:
    print("Acertou!!!")
else:
    print("Errou!!!")

print(f"Seu número: {numero}! O número gerado: {numeroAleatorio}.")