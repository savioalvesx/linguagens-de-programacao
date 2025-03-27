""" enquanto
While - O while repete o bloco de código enquanto a condição for verdadeira e para quando ela se torna falsa.

Sintaxe básica:
    while condição:
        bloco_de_código

"""
contador = 5

while contador > 0:                #1. contador = 5: A condição contador > 0 é verdadeira. O valor 5 é impresso.
    print(f"Contagem: {contador}") #2. contador -= 1: Agora contador vale 4.
    contador -= 1                  #3. Repete o processo até que contador chegue a 0, quando a condição se torna falsa, encerrando o laço.
    #contador = contador - 1 

senha = ""
while senha != "1234":
    senha = input("Digiate a senha: ")
print("Acesso liberado!!")