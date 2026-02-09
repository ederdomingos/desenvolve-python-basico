import csv

# ===============================
# UTILIDADES DE ARQUIVO
# ===============================

def carregar_usuarios():
    usuarios = []
    with open("usuarios.csv", newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            usuarios.append(linha)
    return usuarios


def salvar_usuarios(usuarios):
    with open("usuarios.csv", "w", newline="", encoding="utf-8") as arquivo:
        campos = ["id", "login", "senha", "tipo"]
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(usuarios)


def carregar_produtos():
    produtos = []
    with open("produtos.csv", newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            produtos.append(linha)
    return produtos


def salvar_produtos(produtos):
    with open("produtos.csv", "w", newline="", encoding="utf-8") as arquivo:
        campos = ["id", "nome", "preco", "quantidade"]
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(produtos)

# ===============================
# LOGIN
# ===============================

def login():
    usuarios = carregar_usuarios()
    login = input("Login: ")
    senha = input("Senha: ")

    for u in usuarios:
        if u["login"] == login and u["senha"] == senha:
            print(f"\nBem-vindo, {u['tipo']}!\n")
            return u["tipo"]

    print("Login inválido!")
    return None

# ===============================
# CRUD USUÁRIOS
# ===============================

def listar_usuarios():
    usuarios = carregar_usuarios()
    for u in usuarios:
        print(u)

def criar_usuario():
    usuarios = carregar_usuarios()
    novo = {
        "id": str(len(usuarios) + 1),
        "login": input("Login: "),
        "senha": input("Senha: "),
        "tipo": input("Tipo: ")
    }
    usuarios.append(novo)
    salvar_usuarios(usuarios)

def remover_usuario():
    usuarios = carregar_usuarios()
    login = input("Login para remover: ")
    usuarios = [u for u in usuarios if u["login"] != login]
    salvar_usuarios(usuarios)

# ===============================
# CRUD PRODUTOS
# ===============================

def listar_produtos():
    produtos = carregar_produtos()
    for p in produtos:
        print(p)

def criar_produto():
    produtos = carregar_produtos()
    novo = {
        "id": str(len(produtos) + 1),
        "nome": input("Nome: "),
        "preco": input("Preço: "),
        "quantidade": input("Quantidade: ")
    }
    produtos.append(novo)
    salvar_produtos(produtos)

def buscar_produto():
    produtos = carregar_produtos()
    nome = input("Nome do produto: ").lower()
    for p in produtos:
        if nome in p["nome"].lower():
            print(p)

def ordenar_por_nome():
    produtos = carregar_produtos()
    produtos.sort(key=lambda x: x["nome"])
    for p in produtos:
        print(p)

def ordenar_por_preco():
    produtos = carregar_produtos()
    produtos.sort(key=lambda x: float(x["preco"]))
    for p in produtos:
        print(p)

# ===============================
# MENU
# ===============================

def menu(tipo):
    while True:
        print("\n1 - Listar produtos")
        print("2 - Buscar produto")
        print("3 - Ordenar por nome")
        print("4 - Ordenar por preço")

        if tipo == "gerente":
            print("5 - Criar produto")
            print("6 - Listar usuários")
            print("7 - Criar usuário")
            print("8 - Remover usuário")

        print("0 - Sair")
        opcao = input("Opção: ")

        if opcao == "1":
            listar_produtos()
        elif opcao == "2":
            buscar_produto()
        elif opcao == "3":
            ordenar_por_nome()
        elif opcao == "4":
            ordenar_por_preco()
        elif opcao == "5" and tipo == "gerente":
            criar_produto()
        elif opcao == "6" and tipo == "gerente":
            listar_usuarios()
        elif opcao == "7" and tipo == "gerente":
            criar_usuario()
        elif opcao == "8" and tipo == "gerente":
            remover_usuario()
        elif opcao == "0":
            break
        else:
            print("Opção inválida")

# ===============================
# PROGRAMA PRINCIPAL
# ===============================

tipo_usuario = login()
if tipo_usuario:
    menu(tipo_usuario)

