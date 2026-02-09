numero = input("Digite o número: ")

# remove qualquer caractere não numérico
numero = numero.replace("-", "").replace(" ", "")

if len(numero) == 8:
    numero = "9" + numero

if len(numero) == 9 and numero[0] == "9":
    print(f"Número completo: {numero[:5]}-{numero[5:]}")
else:
    print("Número inválido")
