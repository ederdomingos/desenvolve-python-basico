# Solicita a idade do participante
idade = int(input("Digite sua idade: "))

# Pergunta se já jogou pelo menos 3 jogos de tabuleiro (True ou False)
ja_jogou_3 = input("Já jogou pelo menos 3 jogos de tabuleiro? ") == "True"

# Pergunta quantos jogos já venceu
vitorias = int(input("Quantos jogos já venceu? "))

# Verifica se o participante cumpre todos os critérios de ingresso
apto = (16 <= idade <= 18) and ja_jogou_3 and (vitorias >= 1)

# Imprime o resultado
print("Apto para ingressar no clube de jogos de tabuleiro:", apto)

