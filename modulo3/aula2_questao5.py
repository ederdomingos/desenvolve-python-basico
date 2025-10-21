# Solicita o gênero do usuário
genero = input("Digite seu gênero (M ou F): ").upper()

# Solicita a idade do usuário
idade = int(input("Digite sua idade: "))

# Solicita o tempo de serviço em anos
tempo_servico = int(input("Digite seu tempo de serviço (anos): "))

# Verifica as condições de aposentadoria
aposentadoria = (
    (genero == "F" and idade > 60) or
    (genero == "M" and idade > 65) or
    (tempo_servico >= 30) or
    (idade >= 60 and tempo_servico >= 25)
)

# Imprime True se puder se aposentar, False caso contrário
print(aposentadoria)
