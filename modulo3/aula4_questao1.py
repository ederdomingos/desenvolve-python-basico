# Lê o primeiro número
num1 = int(input("Digite o primeiro número: "))

# Lê o segundo número
num2 = int(input("Digite o segundo número: "))

# Calcula a soma
soma = num1 + num2

# Verifica se a soma é par ou ímpar
if soma % 2 == 0:
    print("A soma é par.")
else:
    print("A soma é ímpar.")