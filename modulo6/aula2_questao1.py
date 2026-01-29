import random

lista = [random.randint(-100, 100) for _ in range(20)]

lista_ordenada = sorted(lista)

print("Lista ordenada (sem alterar a original):")
print(lista_ordenada)

print("\nLista original:")
print(lista)

print("\nÍndice do maior valor:", lista.index(max(lista)))
print("Índice do menor valor:", lista.index(min(lista)))
