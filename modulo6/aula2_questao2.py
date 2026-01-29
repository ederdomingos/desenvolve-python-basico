import random

num_elementos = random.randint(5, 20)
elementos = [random.randint(1, 10) for _ in range(num_elementos)]

print("Lista elementos:")
print(elementos)

soma = sum(elementos)
media = soma / len(elementos)

print("\nSoma dos valores:", soma)
print("Média dos valores:", media)
