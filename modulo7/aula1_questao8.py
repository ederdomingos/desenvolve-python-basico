cpf = input("Digite o CPF (XXX.XXX.XXX-XX): ")

# limpa CPF
cpf_numeros = cpf.replace(".", "").replace("-", "")

if len(cpf_numeros) != 11 or cpf_numeros == cpf_numeros[0] * 11:
    print("Inválido")
else:
    numeros = [int(d) for d in cpf_numeros]

    # primeiro dígito
    soma1 = sum(numeros[i] * (10 - i) for i in range(9))
    resto1 = soma1 % 11
    dig1 = 0 if resto1 < 2 else 11 - resto1

    # segundo dígito
    soma2 = sum(numeros[i] * (11 - i) for i in range(10))
    resto2 = soma2 % 11
    dig2 = 0 if resto2 < 2 else 11 - resto2

    if dig1 == numeros[9] and dig2 == numeros[10]:
        print("Válido")
    else:
        print("Inválido")
