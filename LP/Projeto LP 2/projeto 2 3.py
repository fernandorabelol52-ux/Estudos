# PROJETO 3 - SISTEMA DE GERENCIAMENTO DE ORDENS DE SERVIÇO DE UMA OFICINA

ordens = [  #[numero_os, cliente, equipamento, servico, preco, status]
    [1, "Carlos", "Notebook", "Troca de teclado", 180.00, "Aberta"],
    [2, "Mariana", "Impressora", "Limpeza e revisão", 120.00, "Concluída"]
]

def cadastrar_ordem(ordens): #1
    print("\n--- Cadastrar nova ordem ---")

    numero = len(ordens) + 1 #sistema gera o numero da ordem
    
    cliente = input("Cliente: ")
    equipamento = input("Equipamento: ")
    servico = input("Descrição do Serviço: ")
    preco = float(input("Preço: "))

    nova_ordem = [numero, cliente, equipamento, servico, preco, "Aberta"] 
    ordens.append(nova_ordem)

    print(f"Ordem nº {numero} cadastrada com sucesso!")

def consultar_ordem(ordens): #2
    print("\n--- Consultar ordem ---")

    numero = int(input("Numero da ordem: "))

    for ordem in ordens:
        if ordem[0] == numero:
            print(f"\nOrdem de serviço: {ordem[0]}")
            print(f"Cliente: {ordem[1]}")
            print(f"Equipamento: {ordem[2]}")
            print(f"Serviço: {ordem[3]}")
            print(f"Preço: R$ {ordem[4]:.2f}")
            print(f"Status: {ordem[5]}")
            print("-" * 32)
            return 
    print("Ordem não encontrada!")

def alterar_status(ordens): #3
    print("\n--- Alterar status ---")

    numero = int(input("Numero da ordem: "))

    for ordem in ordens:
        if ordem[0] == numero:
            print(f"\nStatus da ordem: {ordem[5]}")
            print("1 - Aberta")
            print("2 - Em andamento")
            print("3 - Concluída")
            
            alterar = input("Deseja alterar? (S/N)")
            
            if alterar == "S":
                opcao = input("Novo status: ")

                if opcao == "1":
                    ordem[5] = "Aberta"
                elif opcao == "2":
                    ordem[5] = "Em andamento"
                elif opcao == "3":
                    ordem[5] = "Concluída"
                else:
                    print("Status atualizado com sucesso!")
                    return
            
            elif alterar == "N":
                print("Nenhuma alteração feita.")
                return
            else:
                print("Opção inválida!")
                return

def listar_ordens(ordens): #4
    print("\n--- Todas as ordens ---")

    if len(ordens) == 0:
        print("Nenhuma ordem cadastrada.")
        return
    
    print(f"Total de ordens cadastradas: {len(ordens)}")

    for ordem in ordens:
        print(f"\nOrdem de serviço: {ordem[0]}")
        print(f"Cliente: {ordem[1]}")
        print(f"Equipamento: {ordem[2]}")
        print(f"Serviço: {ordem[3]}")
        print(f"Preço: R$ {ordem[4]:.2f}")
        print(f"Status: {ordem[5]}")
        print("-" * 32)

def listar_pendentes(ordens): #5
    print("\n--- Ordens pendentes ---")

    pendentes = 0

    for ordem in ordens:
        if ordem[5] != "Concluída":
            print(f"\nOrdem de serviço: {ordem[0]}")
            print(f"Cliente: {ordem[1]}")
            print(f"Equipamento: {ordem[2]}")
            print(f"Serviço: {ordem[3]}")
            print(f"Preço: R$ {ordem[4]:.2f}")
            print(f"Status: {ordem[5]}")
            print("-" * 32)
            pendentes += 1
    if pendentes == 0:
        print("Nenhuma ordem pendente.")
    else:
        print(f"\nTotal de ordens pendentes: {pendentes}")

def total_concluidas(ordens): #6
    print("\n--- Valor total das ordens concluídas ---")

    total = 0.0
    quantidade = 0

    for ordem in ordens:
        if ordem[5] == "Concluída":
            total += ordem[4]
            quantidade += 1
    if quantidade == 0:
        print("Nenhuma ordem concluída ainda.")
    else:
        print(f"Ordens concluídas: {quantidade}")
        print(f"Valor total: R$ {total:.2f}")

def ordenar_precos(ordens): #7
    print("\n--- Ordens ordenadas por preço (maior para menor) ---")

    if len(ordens) == 0:
        print("Nenhuma ordem cadastrada.")
        return
    
    lista = [ordem[:] for ordem in ordens]

    n = len(lista)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista [j][4] < lista[j + 1][4]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    
    for ordem in lista:
        print(f"\nOrdem de serviço: {ordem[0]}")
        print(f"Cliente: {ordem[1]}")
        print(f"Equipamento: {ordem[2]}")
        print(f"Serviço: {ordem[3]}")
        print(f"Preço: R$ {ordem[4]:.2f}")
        print(f"Status: {ordem[5]}")
        print("-" * 32)

def contar_por_status(ordens):
    print("\n--- Ordens por status ---")
    
    if len(ordens) == 0:
        print("Nenhuma ordem cadastrada.")
        return
    
    abertas = 0
    em_andamento = 0
    concluidas = 0
    
    for ordem in ordens:
        if ordem[5] == "Aberta":
            abertas += 1
        elif ordem[5] == "Em andamento":
            em_andamento += 1
        elif ordem[5] == "Concluída":
            concluidas += 1
    
    print(f"Ordens abertas: {abertas}")
    print(f"Ordens em andamento: {em_andamento}")
    print(f"Ordens concluídas: {concluidas}")

while True:
    print("\n===== ORDENS DE SERVIÇO =====")
    print("1 - Cadastrar nova ordem")
    print("2 - Consultar ordem pelo número")
    print("3 - Alterar status")
    print("4 - Listar todas as ordens")
    print("5 - Listar ordens pendentes")
    print("6 - Valor total das ordens concluídas")
    print("7 - Ordenar por preço (decrescente)")
    print("8 - Sair")
    
    opcao = input("\nEscolha uma opção: ")
    
    if opcao == "1":
        cadastrar_ordem(ordens) 
    elif opcao == "2":
        consultar_ordem(ordens)
    elif opcao == "3":
        alterar_status(ordens)
    elif opcao == "4":
        listar_ordens(ordens)
    elif opcao == "5":
        listar_pendentes(ordens)
    elif opcao == "6":
        total_concluidas(ordens)
    elif opcao == "7":
        ordenar_precos(ordens)
    elif opcao == "8":
        print("Encerrando...")
        break
    else:
        print("Opção Inválida!")









            

            





