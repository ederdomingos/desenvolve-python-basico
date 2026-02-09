with open("estomago.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

# primeiras 25 linhas
print("Primeiras 25 linhas:\n")
for linha in linhas[:25]:
    print(linha.rstrip())

print("\nNúmero total de linhas:", len(linhas))

linha_maior = max(linhas, key=len)
print("\nLinha com mais caracteres:\n", linha_maior)

texto = "".join(linhas).lower()

nonato = texto.count("nonato")
iria = sum(1 for palavra in texto.split() if palavra.strip(".,!?") == "íria" or palavra.strip(".,!?") == "iria")

print("\nMenções a Nonato:", nonato)
print("Menções a Íria:", iria)
