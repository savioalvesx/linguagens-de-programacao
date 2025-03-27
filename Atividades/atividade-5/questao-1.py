texto = input("Informe um texto: ")
palavraEspecifica = input("\nInforme a palavra que deseja contar: ")

caracterTotal = len(texto)
palavras = texto.split()
numeroPalavras = len(palavras)
numeroPalavraEspecifica = palavras.count(palavraEspecifica)


print(f"\nO número total de caracteres: {caracterTotal}")
print(f"O número de palavras: {numeroPalavras}")
print(f"A quantidade de vezes que a palavra '{palavraEspecifica}' aparece: {numeroPalavraEspecifica}")