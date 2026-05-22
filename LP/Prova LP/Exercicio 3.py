total_alunnos = 0
notas5 = 0
notas1 = 0
soma_nota = 0

print("Pesquias de Satisfação")

while True:
    nota = int(input("Informe uma nota de 1 a 5 (Digite 0 para sair): "))

    if nota == 0:
        break

    if 1 <= nota <= 5:
        total_alunnos += 1
        soma_nota += nota

        if nota == 5:
            notas5 += 1
        elif nota == 1:
            notas1 += 1
    else:
        print("Nota invalida")
if total_alunnos > 0:
    media = soma_nota / total_alunnos

    print("\n    Resultado da Pesquisa")
    print(f"Quantidade de alunnos que responderam: {total_alunnos}")
    print (f"Quantidade de notas 5: {notas5}")
    print (f"Quantidade de notas 1: {notas1}")
    print (f"Média das notas informadas: {media:.2f}")
else:
    print("Nenhuma nota valida foi informada")