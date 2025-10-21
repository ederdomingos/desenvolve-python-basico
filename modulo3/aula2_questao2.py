# Solicita a idade de Juliana
idade_juliana = int(input("Digite a idade de Juliana: "))

# Solicita a idade de Cris
idade_cris = int(input("Digite a idade de Cris: "))

# Verifica se pelo menos uma é maior de 17 anos
pode_entrar = idade_juliana > 17 or idade_cris > 17

# Imprime True se puderem entrar, False caso contrário
print(pode_entrar)
