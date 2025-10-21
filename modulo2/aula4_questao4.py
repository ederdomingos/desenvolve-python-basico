# Lê o valor em reais como inteiro
valor = int(input("Digite o valor em reais: "))

# Lista das cédulas disponíveis
notas = [100, 50, 20, 10, 5, 2, 1]

# Para cada nota, calcula a quantidade necessária e atualiza o valor restante
for nota in notas:
    quantidade = valor // nota  # Divisão inteira
    print(f"{quantidade} nota(s) de R${nota},00")
    valor = valor % nota  # Resto para as próximas notas
