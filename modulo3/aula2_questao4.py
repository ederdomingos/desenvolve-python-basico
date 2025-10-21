# Solicita a classe do personagem
classe = input("Escolha a classe (guerreiro, mago ou arqueiro): ").lower()

# Solicita os pontos de força e magia
forca = int(input("Digite os pontos de força (de 1 a 20): "))
magia = int(input("Digite os pontos de magia (de 1 a 20): "))

# Verifica se os pontos são consistentes com a classe escolhida
if classe == "guerreiro":
    consistente = (forca >= 15) and (magia <= 10)
elif classe == "mago":
    consistente = (forca <= 10) and (magia >= 15)
elif classe == "arqueiro":
    consistente = (forca > 5 and forca <= 15) and (magia > 5 and magia <= 15)
else:
    consistente = False  # Caso a classe digitada seja inválida

# Imprime o resultado
print("Pontos de atributo consistentes com a classe escolhida:", consistente)