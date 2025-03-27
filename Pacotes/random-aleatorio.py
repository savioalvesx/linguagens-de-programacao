import random

numeroAleatorio = random.randint(0,10)

numero = int(input("Informe um número de 0 a 10: "))

if numeroAleatorio == numero:
    print("Acertou!!!")
else:
    print("Errou!!!")

print(f"Seu número: {numero}!\nO número sorteado: {numeroAleatorio}!")