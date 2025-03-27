print("Este programa verifica se uma letra é Vocal ou Consoante.\n")

letra = str(input("Informe uma letra: ")).upper()

if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
    print(f"A letra {letra} é uma vogal.")
else:
    print(f"A letra {letra} é uma consoante.")