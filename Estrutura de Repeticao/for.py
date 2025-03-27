""" para
for - O for em Python é usado para percorrer elementos de uma sequência (como listas, strings ou intervalos). 
A cada iteração, ele atribui um item da sequência a uma variável e executa um bloco de código.

Sintaxe básica:
    for variável in sequência:
    bloco_de_código

"""

#for utilizando o range.
for i in range(1,101): #Vai de 1 até 100. 
    print(f"Número: {i}")

print("\n")

#for com strings.
nome = "Alvaro"
for letra in nome:
    print(letra)

print("\n")

#for utilizando listas
frutas = ["banana", "maçã", "abacaxi", 30]
for item in frutas:
    print(item)

print("\n")

for i in range(1, 11):
    if i == 5:
        break
    print(i)

print ("\n")

for i in range(1, 11):
    if i == 5:
        continue
    print(i)
