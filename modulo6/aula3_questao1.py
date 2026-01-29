numeros = []

print("Digite números inteiros (mínimo 4). Digite 'sair' para encerrar.")

while True:
    entrada = input("Número: ")
    if entrada.lower() == "sair":
        if len(numeros) < 4:
            print("Digite pelo menos 4 números.")
            continue
        break
    numeros.append(int(entrada))

print("\nLista original:")
print(numeros)

print("\n3 primeiros elementos:")
print(numeros[:3])

print("\n2 últimos elementos:")
print(numeros[-2:])

print("\nLista invertida:")
print(numeros[::-1])

print("\nElementos de índice par:")
print(numeros[::2])

print("\nElementos de índice ímpar:")
print(numeros[1::2])
