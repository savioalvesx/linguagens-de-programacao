texto = input("Informe um texto: ")
palavraOriginal = input("\nInforme a palavra que deseja substituir: ")
palavraSubstituta = input("\nInforme a palavra para substituir a original: ")

textoModificada = texto.replace(palavraOriginal, palavraSubstituta)

print(f"\nTexto original: {texto}")
print(f"Texto modificada: {textoModificada}")