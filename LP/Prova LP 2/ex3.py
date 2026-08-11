pedidos = []

def cadastrar_pedido(pedidos):
    print("\n1 - Registrar pedido")
    numero = int(input("Digite o numero do pedido: "))
    for pedido in pedidos:
        if pedido[0] == numero:
            print("Pedido ja cadastrado!")
            return
    cliente = input("Digite o nome do cliente: ")
    produtos = input("Digite o produto: ")
    quant = int(input("Digite a quantidade: "))
    valor_uni = float(input("Digite o preço unitário do produto: "))
    status = "Recebido"
    pedidos.append([numero, cliente, produtos, quant, valor_uni, status])
    print("Pedido cadastrado com sucesso!")

def consultar_pedido(pedidos):
    print("\n2 - Consultar pedido pelo numero")
    numero = int(input("Digite o numero do pedido: "))
    for pedido in pedidos:
        if pedido[0] == numero:
            print(f"\nNumero do pedido: {pedido[0]}")
            print(f"Cliente: {pedido[1]}")
            print(f"Produto: {pedido[2]}")
            print(f"Quantidade: {pedido[3]}")
            print(f"Preço unitário: R${pedido[4]:.2f}")
            print(f"Status: {pedido[5]}")
            print("-" * 20)
            return
    print("Pedido nao encontrado!")

def alterar_status(pedidos):
    print("\n3 - Alterar status")
    numero = int(input("Digite o numero do pedido: "))
    for pedido in pedidos:
        if pedido[0] == numero:
            print("\n1 - Recebido")
            print("2 - Em preparo")
            print("3 - Entregue")
            print("4 - Cancelado")
            status = int(input("Digite o novo status do pedido: "))
            if status == 1:
                pedido[5] = "Recebido"
            elif status == 2:
                pedido[5] = "Em preparo"
            elif status == 3:
                pedido[5] = "Entregue"
            elif status == 4:
                pedido[5] = "Cancelado"
            print(f"Status alterado com sucesso para {pedido[5]}!")
            return
    print("Pedido nao encontrado!")

def listar_pedidos(pedidos):
    print("\n4 - Listar todos os pedidos")
    for pedido in pedidos:
        print(f"\nNumero do pedido: {pedido[0]}")
        print(f"Cliente: {pedido[1]}")
        print(f"Produto: {pedido[2]}")
        print(f"Quantidade: {pedido[3]}")
        print(f"Preço unitário: R${pedido[4]:.2f}")
        print(f"Status: {pedido[5]}")
        print("-" * 20)

def listar_pendente(pedidos):
    print("\n5 - Listar apenas pedidos pendentes")
    for pedido in pedidos:
        if pedido[5] == "Recebido" or "Em preparo":
            print(f"\nNumero do pedido: {pedido[0]}")
            print(f"Cliente: {pedido[1]}")
            print(f"Produto: {pedido[2]}")
            print(f"Quantidade: {pedido[3]}")
            print(f"Preço unitário: R${pedido[4]:.2f}")
            print(f"Status: {pedido[5]}")
            print("-" * 20)

def exibir_financeiro(pedidos):
    print("\n6 - Exibir resumo financeiro")
    total = 0
    num_total = 0
    num_entre = 0
    num_cance = 0
    valor_medio = 0
    for pedido in pedidos:
        num_total += 1
        if pedido[5] == "Entregue":
            num_entre += 1
        elif pedido[5] == "Cancelado":
            num_cance += 1
    for pedido in pedidos:
        if pedido[5] == "Entregue":
            total += (pedido[3] * pedido[4])
    valor_medio = total / num_entre
    print(f"Valor total: R${total:.2f}")
    print(f"Numero total de pedidos: {num_total}")
    print(f"Numero de pedidos entregues: {num_entre}")
    print(f"Numero de pedidos cancelados: {num_cance}")
    print(f"Valor medio de pedidos entregues: R${valor_medio:.2f}")

def ordenar_pedidos(pedidos):
    print("\n7 - Ordenar pedidos pelo valor total")
    final = len(pedidos)
    while final >= 1:
        trocou = False
        x = 0
        while x < (final - 1):
            valor_atual = (pedidos[x][3] * pedidos[x][4])
            valor_proximo = (pedidos[x + 1][3] * pedidos[x + 1][4])
            
            if valor_atual < valor_proximo:
                trocou = True
                temp = pedidos[x]
                pedidos[x] = pedidos[x + 1]
                pedidos[x + 1] = temp
            x += 1
        if not trocou:
            break
        final -= 1
    listar_pedidos(pedidos)


while True:
    print ("LANCHONETE")
    print("\n1 - Registrar pedido")
    print("2 - Consultar pedido pelo numero")
    print("3 - Alterar status")
    print("4 - Listar todos os pedidos")
    print("5 - Listar apenas pedidos pendentes")
    print("6 - Exibir resumo financeiro")
    print("7 - Ordenanr pedidos pelo valor total")
    print("8 - Sair")



    print("")

    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        cadastrar_pedido(pedidos)
    elif opcao == 2:
        consultar_pedido(pedidos)
    elif opcao == 3:
        alterar_status(pedidos)
    elif opcao == 4:
        listar_pedidos(pedidos)
    elif opcao == 5:
        listar_pendente(pedidos)
    elif opcao == 6:
        exibir_financeiro(pedidos)
    elif opcao == 7:
        ordenar_pedidos(pedidos)
    elif opcao == 8:
        break
    else:
        print("Opção inválida! Tente novamente.")