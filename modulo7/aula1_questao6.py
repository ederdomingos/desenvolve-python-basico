frase = input("Digite uma frase: ")
palavra_objetivo = input("Digite a palavra objetivo: ")

alvo_ordenado = sorted(palavra_objetivo.lower())
resultado = []

for palavra in frase.split():
    palavra_limpa = palavra.strip(".,!?:;").lower()
    if sorted(palavra_limpa) == alvo_ordenado:
        resultado.append(palavra)

print("Anagramas:", resultado)
