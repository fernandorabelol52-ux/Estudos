produtos = [[101, "Arroz", 20, 25.90], [102, "Feijão", 15, 8.75], [103, "Leite", 30, 5.80], [104, "Café", 8, 18.50]]

def listar_produtos(produtos):
    for prod in produtos:
        print(f"Codigo do produto: {prod[0]}")
        print(f"Produto: {prod[1]}")
        print(f"Estoque: {prod[2]}")
        print(f"Preço: R${prod[3]:.2f}")
        print(f"Valor armazenado: R${prod[2] * prod[3]:.2f}")
        print("-" * 20)

def consulta_codigo(produtos):
    codigo = int(input("Digite o código do produto: "))
    for prod in produtos:
        if prod[0] == codigo:
            print(f"Codigo do produto: {prod[0]}")
            print(f"Produto: {prod[1]}")
            print(f"Estoque: {prod[2]}")
            print(f"Preço: R${prod[3]:.2f}")
            print(f"Valor armazenado: R${prod[2] * prod[3]:.2f}")
            print("-" * 20)
            return
    print("Produto não encontrado!")

def regist_entrada(produtos):
    codigo = int(input("Digite o código do produto: "))
    for prod in produtos:
        if prod[0] == codigo:
            quantidade = int(input("Digite a quantidade a ser adicionada: "))
            prod[2] += quantidade
            print("Entrada registrada com sucesso!")
            return
    print("Produto não encontrado!")

def regist_saida(produtos):
    codigo = int(input("Digite o código do produto: "))
    for prod in produtos:
        if prod[0] == codigo:
            quantidade = int(input("Digite a quantidade a ser retirada: "))
            prod[2] -= quantidade
            print("Saída registrada com sucesso!")
            return
    print("Produto não encontrado!")

def cadast_novo(produtos):
    codigo = int(input("Digite o código do novo produto: "))
    for prod in produtos:
        if prod[0] == codigo:
            print("Produto já cadastrado!")
            return
    nome = input("Digite o nome do novo produto: ")
    estoque = int(input("Digite a quantidade inicial do novo produto: "))
    preco = float(input("Digite o preço do novo produto: "))
    produtos.append([codigo, nome, estoque, preco])
    print("Novo produto cadastrado com sucesso!")

def relatorio(produtos):
    total = 0
    quantidade = 0
    quant_prod = 0
    maior_valor = 0
    nome_maior = ""
    
    for prod in produtos:
        quantidade += prod[2]
    for prod in produtos:
        total += (prod[2] * prod[3])
    for prod in produtos:
        quant_prod += 1
    for prod in produtos:
        valor_estoque = prod[2] * prod[3]
        if valor_estoque > maior_valor:
            maior_valor = valor_estoque
            nome_maior = prod[1]

    print("\nRelatório financeiro do estoque:")
    print(f"Quantidade total de unidades: {quantidade}")
    print(f"Quantidade de produtos cadastrados diferentes: {quant_prod}")
    print(f"Valor total armazenado: R${total:.2f}")
    print(f"Produto com maior valor armazenado: {nome_maior} (R${maior_valor:.2f})")

    print("")

while True:
    print("\nCONTROLE DE ESTOQUE")
    print("1 - Listar produtos")
    print("2 - Consultar produto pelo código")
    print("3 - Registrar entrada de mercadoria")
    print("4 - Registrar saída de mercadoria")
    print("5 - Cadastrar novo produto")
    print("6 - Exibir relatório financeiro do estoque")
    print("7 - Sair")

    opção = int(input("Escolha uma opção: "))

    if opção == 1:
        listar_produtos(produtos)
    elif opção == 2:
        consulta_codigo(produtos)
    elif opção == 3:
        regist_entrada(produtos)
    elif opção == 4:
        regist_saida(produtos)
    elif opção == 5:
        cadast_novo(produtos)
    elif opção == 6:
        relatorio(produtos)
    elif opção == 7:
        break
    else:
        print("Opção inválida! Tente novamente.")