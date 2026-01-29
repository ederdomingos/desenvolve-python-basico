# Remover espaços e ignorar strings vazias
dados = ["  Python  ", "", "  Listas", " ", "Compreensao  "]
limpos = [d.strip() for d in dados if d.strip()]
print(limpos)
