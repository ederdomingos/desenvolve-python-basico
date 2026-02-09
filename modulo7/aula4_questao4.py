import random

def imprime_enforcado(erros, estagios):
    print(estagios[erros])

with open("gabarito_forca.txt", "r", encoding="utf-8") as f:
    palavras = [p.strip().lower() for p in f.readlines()]

with open("gabarito_enforcado.txt", "r", encoding="utf-8") as f:
    estagios = f.read().split("\n\n")

palavra = random.choice(palavras)
progresso = ["_"] * len(palavra)
tentativas = 0
usadas = set()

while tentativas < 6 and "_" in progresso:
    print("\nPalavra:", " ".join(progresso))
    letra = input("Digite uma letra: ").lower()

    if letra in usadas:
        continue

    usadas.add(letra)

    if letra in palavra:
        for i, c in enumerate(palavra):
            if c == letra:
                progresso[i] = letra
    else:
        tentativas += 1
        imprime_enforcado(tentativas, estagios)

if "_" not in progresso:
    print("\nParabéns! Palavra:", palavra)
else:
    print("\nVocê perdeu! Palavra:", palavra)
