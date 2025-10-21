# Lê o comprimento do terreno (em metros) como inteiro
comprimento = int(input("Digite o comprimento do terreno (m): "))

# Lê a largura do terreno (em metros) como inteiro
largura = int(input("Digite a largura do terreno (m): "))

# Lê o preço do metro quadrado da região como número de ponto flutuante
preco_m2 = float(input("Digite o preço do metro quadrado (R$): "))

# Calcula a área do terreno em metros quadrados
area_m2 = comprimento * largura

# Calcula o preço total do terreno
preco_total = preco_m2 * area_m2

# Imprime o resultado formatado com duas casas decimais
print("O terreno possui {}m2 e custa R${:.2f}".format(area_m2, preco_total))
