print("Este programa soma todos os números informados.")

soma = 0

for i in range(5): #range(1, 6)
    numero = int(input(f"Informe o {i+1}º Número: "))
    soma += numero

print(f"Soma Total: {soma}")

"""
soma = soma + numero: Nessa expressão, o valor atual de soma é somado ao valor de numero, e o resultado é armazenado de volta na variável soma. Ou seja, a cada interação do loop, a variável soma vai acumulando os valores fornecidos pelo usuário.

soma += numero: Esse é um operador abreviado para a soma. Ele faz exatamente o mesmo que soma = soma + numero, mas de forma mais compacta e legível. 
É um exemplo de um operador de atribuição composta, que é uma maneira prática de realizar operações matemáticas com a variável que está sendo manipulada.

Assim, a cada vez que o usuário informa um número, ele vai sendo adicionado à variável soma, e ao final do loop, você terá a soma total de todos os números informados.

Exemplo:

O usuário informa o número 5.
A variável soma que inicialmente é 0 passa a ser 5.
O usuário informa o número 3.
Agora, soma será 8 (5 + 3).
E assim por diante até o final do loop.

"""