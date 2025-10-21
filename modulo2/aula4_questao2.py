# Lê a temperatura em Fahrenheit como inteiro
fahrenheit = int(input("Digite a temperatura em Fahrenheit: "))

# Converte para Celsius usando a fórmula e arredonda para inteiro
celsius = int(round((fahrenheit - 32) * (5/9)))

# Imprime o resultado no formato solicitado
print(f"{fahrenheit} graus Fahrenheit são {celsius} graus Celsius.")