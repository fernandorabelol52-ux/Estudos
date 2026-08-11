alunos = []

def situacao(nota1, nota2):
    media = (nota1 + nota2) / 2
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperacao"
    else:
        return "Reprovado"

def cadastrar_aluno(alunos):
    
    print("\n1 - Cadastrar aluno")
    matricula = int(input("Digite a matricula do aluno: "))
    nome = input("Digite o nome do aluno: ")
    
    while True:
        nota1 = float(input("Digite a primeira nota: "))
        if 0.0 <= nota1 <= 10.0:
            break
        print("Nota inválida! A nota deve estar entre 0.0 e 10.0.")
        
    while True:
        nota2 = float(input("Digite a segunda nota: "))
        if 0.0 <= nota2 <= 10.0:
            break
        print("Nota inválida! A nota deve estar entre 0.0 e 10.0.")
        
    situacao = situacao(nota1, nota2)
    alunos.append([matricula, nome, nota1, nota2, situacao])
    print("Aluno cadastrado com sucesso!")

def consultar_aluno(alunos):
    print("\n2 - Consultar Aluno pela matricula")
    matricula = int(input("Digite a matricula do aluno: "))
    for aluno in alunos:
        if aluno[0] == matricula:
            print(f"Matricula: {aluno[0]}")
            print(f"Nome: {aluno[1]}")
            print(f"Nota 1: {aluno[2]}")
            print(f"Nota 2: {aluno[3]}")
            print(f"Situacao: {aluno[4]}")
            print("-" * 20)
            return
    print("Aluno nao encontrado!")

def alterar_notas(alunos):
    print("\n3 - Alterar notas")
    matricula = int(input("Digite a matricula do aluno que deseja alterar as notas: "))
    for aluno in alunos:
        if aluno[0] == matricula:
            while True:
                nota1 = float(input("Digite a primeira nota: "))
                if 0.0 < nota1 < 10.0:
                    break
                print("Nota inválida! A nota deve estar entre 0.0 e 10.0.")
                
            while True:
                nota2 = float(input("Digite a segunda nota: "))
                if 0.0 < nota2 < 10.0:
                    break
                print("Nota inválida! A nota deve estar entre 0.0 e 10.0.")
            situacao = situacao(nota1, nota2)
            
            aluno[2] = nota1
            aluno[3] = nota2
            aluno[4] = situacao
            print("Aluno alterado com sucesso!")
            return
    print("Aluno nao encontrado!")

def listar_alunos(alunos):
    print("\n4 - Listar alunos")
    for aluno in alunos:
        print(f"Matricula: {aluno[0]}")
        print(f"Nome: {aluno[1]}")
        print(f"Nota 1: {aluno[2]}")
        print(f"Nota 2: {aluno[3]}")
        print(f"Situacao: {aluno[4]}")
        print("-" * 20)

def mostrar_estatistica(alunos):
    print("\n5 - Mostrar estatistica da turma")
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    
    total = 0
    cont1 = 0
    cont2 = 0
    cont3 = 0
    contagem = 0
    
    for aluno in alunos:
        total += (aluno[2] + aluno[3]) / 2
        if total >= 7:
            cont1 +=1
        elif total >= 5:
           cont2 += 1
        else:
            cont3 += 1
        contagem = cont1 + cont2 + cont3
    media = total / len(alunos)
    print("")
    print(f"Total de alunos: {contagem}")
    print(f"Aprovados: {cont1}")
    print(f"Recuperacao: {cont2}")
    print(f"Reprovados: {cont3}")
    print(f"Media da turma: {media:.2f}")


def ordenar_alunos(alunos):
    print("\n6 - Ordenar alunos pela media")
    final = len(alunos)
    while final >= 1:
        trocou = False
        x = 0
        while x < (final - 1):
            media_atual = (alunos[x][2] + alunos[x][3]) / 2
            media_proxima = (alunos[x + 1][2] + alunos[x + 1][3]) / 2
            
            if media_atual < media_proxima:
                trocou = True
                temp = alunos[x]
                alunos[x] = alunos[x + 1]
                alunos[x + 1] = temp
            x += 1
        if not trocou:
            break
        final -= 1
    listar_alunos(alunos)




while True:
    print ("SISTEMA ACADEMICO")
    print("\n1 - Cadastrar aluno")
    print("2 - Consultar Aluno pela matricula")
    print("3 - Alterar notas")
    print("4 - Listar alunos")
    print("5 - Mostrar estatistica da turma")
    print("6 - Ordenar alunos pela média")
    print("7 - Sair")



    print("")

    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        cadastrar_aluno(alunos)
    elif opcao == 2:
        consultar_aluno(alunos)
    elif opcao == 3:
        alterar_notas(alunos)
    elif opcao == 4:
        listar_alunos(alunos)
    elif opcao == 5:
        mostrar_estatistica(alunos)
    elif opcao == 6:
        ordenar_alunos(alunos)
    elif opcao == 7:
        break
    else:
        print("Opção inválida! Tente novamente.")
    