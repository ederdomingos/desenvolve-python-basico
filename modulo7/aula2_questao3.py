import string

while True:
    frase = input('Digite uma frase (digite "fim" para encerrar): ')

    if frase.lower() == "fim":
        break

    limpa = ""
    for c in frase.lower():
        if c not in string.punctuation and c != " ":
            limpa += c

    if limpa == limpa[::-1]:
        print(f'"{frase}" é palíndromo')
    else:
        print(f'"{frase}" não é palíndromo')
