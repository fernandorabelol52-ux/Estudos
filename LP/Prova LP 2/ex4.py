lugares = list(range(1,21))

def most_lug(lugares):
    print(lugares)

def reser_lug(lugares):
    lugar = int(input("Digite o numero do lugar que deseja reservar: "))
    if lugar in lugares:
        lugares.remove(lugar)
        print(f"Lugar {lugar} reservado com sucesso!")
    else:
        print("Lugar ja reservado!")

def canc_lug(lugares):
    lugar = int(input("Digite o numero do lugar que deseja cancelar a reserva: "))
    if lugar not in lugares:
        lugares.append(lugar)
        print(f"Lugar {lugar} cancelado com sucesso!")
    else:
        print("Lugar nao reservado!")

def cons_lug(lugares):
    lugar = int(input("Digite o numero do lugar que deseja consultar: "))
    if lugar in lugares:
        print(f"Lugar {lugar} esta disponivel!")
    elif lugar < 21:
        print(f"Lugar {lugar} esta reservado!")
    else:
        print("Lugar inesistente!")

def mostrar_rel(lugares):
    qunt_dispo = len(lugares)
    qunt_reserv = 20 - qunt_dispo
    penct_ocup = (qunt_reserv / 20) * 100
    print(f"Quantidade de lugares disponiveis: {qunt_dispo}")
    print(f"Quantidade de lugares reservados: {qunt_reserv}")
    print(f"Percentual de ocupacao: {penct_ocup:.2f}%")
    if qunt_dispo > 0:
        print(f"Menor lugar disponivel: {min(lugares)}")
        print(f"Maior lugar disponivel: {max(lugares)}")
    else:
        print("Nenhum lugar disponivel.")

def ord_lugares(lugares):
    final = len(lugares)
    while final >= 1:
        trocou = False
        x = 0
        while x < (final - 1):
            if lugares[x] > lugares[x + 1]:
                trocou = True
                temp = lugares[x]
                lugares[x] = lugares[x + 1]
                lugares[x + 1] = temp
            x += 1
        if not trocou:
            break
        final -= 1
    print(lugares)

while True:
    print ("RESERVA DE LUGARES")
    print("\n1 - Mostrar lugares disponiveis")
    print("2 - Reservar lugar")
    print("3 - Cancelar reserva")
    print("4 - Consultar situação de um lugar")
    print("5 - Mostrar relatorio")
    print("6 - Ordenar lugares disponiveis")
    print("7 - Sair")
    
    print("")

    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        most_lug(lugares)
    elif opcao == 2:
        reser_lug(lugares)
    elif opcao == 3:
        canc_lug(lugares)
    elif opcao == 4:
        cons_lug(lugares)
    elif opcao == 5:
        mostrar_rel(lugares)
    elif opcao == 6:
        ord_lugares(lugares)
    elif opcao == 7:
        break
    else:
        print("Opção inválida! Tente novamente.")