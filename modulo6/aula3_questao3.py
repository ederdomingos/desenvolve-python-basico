import random

lista = [random.randint(-10, 10) for _ in range(20)]

print("Lista original:")
print(lista)

maior_inicio = maior_fim = -1
inicio_atual = None

for i, valor in enumerate(lista):
    if valor < 0:
        if inicio_atual is None:
            inicio_atual = i
    else:
        if inicio_atual is not None:
            if maior_inicio == -1 or (i - inicio_atual) > (maior_fim - maior_inicio):
                maior_inicio, maior_fim = inicio_atual, i
            inicio_atual = None

if inicio_atual is not None:
    if maior_inicio == -1 or (len(lista) - inicio_atual) > (maior_fim - maior_inicio):
        maior_inicio, maior_fim = inicio_atual, len(lista)

if maior_inicio != -1:
    del lista[maior_inicio:maior_fim]

print("\nLista editada:")
print(lista)
