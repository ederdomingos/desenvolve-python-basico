qtd1 = int(input("Digite a quantidade de elementos da lista 1: "))
lista1 = []

print(f"Digite os {qtd1} elementos da lista 1:")
for _ in range(qtd1):
    lista1.append(int(input()))

qtd2 = int(input("\nDigite a quantidade de elementos da lista 2: "))
lista2 = []

print(f"Digite os {qtd2} elementos da lista 2:")
for _ in range(qtd2):
    lista2.append(int(input()))

lista_intercalada = []

menor = min(len(lista1), len(lista2))

for i in range(menor):
    lista_intercalada.append(lista1[i])
    lista_intercalada.append(lista2[i])

if len(lista1) > len(lista2):
    lista_intercalada.extend(lista1[menor:])
else:
    lista_intercalada.extend(lista2[menor:])

print("\nLista intercalada:")
print(*lista_intercalada)
