import random

def encrypt(nomes):
    chave = random.randint(1, 10)
    criptografados = []

    for nome in nomes:
        novo_nome = ""
        for c in nome:
            codigo = ord(c) + chave
            if codigo > 126:
                codigo = 33 + (codigo - 127)
            novo_nome += chr(codigo)
        criptografados.append(novo_nome)

    return criptografados, chave


nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_cript, chave = encrypt(nomes)

print("Chave:", chave)
print("Nomes criptografados:", nomes_cript)
