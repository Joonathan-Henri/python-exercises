estoque = []


def buscar_produto(codigo):
    for produto in estoque:
        if produto["codigo"] == codigo:
            return produto
    return None


def cadastrar_produto():
    print("\n--- Cadastro de produto ---")

    codigo = int(input("Digite o código: "))

    if buscar_produto(codigo):
        print("Esse código já está cadastrado.")
        return

    nome = input("Digite o nome: ")
    preco = float(input("Digite o preço: "))
    quantidade = int(input("Digite a quantidade: "))

    if preco < 0 or quantidade < 0:
        print("O preço e a quantidade não podem ser negativos.")
        return

    produto = {
        "codigo": codigo,
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }

    estoque.append(produto)

    print("Produto cadastrado com sucesso!")


def calcular_total():
    total = 0

    for produto in estoque:
        total += produto["quantidade"]

    print("\nTotal de produtos em estoque:", total)


while True:
    print("\n--- CONTROLE DE ESTOQUE ---")
    print("1 - Cadastrar Produto")
    print("2 - Calcular Total de Produtos")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_produto()

    elif opcao == "2":
        calcular_total()

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")