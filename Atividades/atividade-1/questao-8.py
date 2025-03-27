print("Programa informa o troco de uma compra.\n")

valor_produto = float(input("Informe o valor do produto: R$ "))
valor_pago = float(input("Informe o valor pago pelo cliente: R$ "))

troco = valor_pago - valor_produto

if troco >= 0:
    print(f"O troco a ser devolvido é: R$ {troco:.2f}")
else:
    print("Valor insuficiente! O valor pago é menor que o valor do produto.")