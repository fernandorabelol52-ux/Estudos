lugares_vagos = [10, 2, 1, 3, 0]

while True:
    sala = int(input("Qual sala de cinema (Digite '0' para sair: "))
    if sala == 0:
        print("Fim")
        break
    if sala > len(lugares_vagos) or sala < 1:
        print("Sala invalida!")
    elif lugares_vagos[sala-1] > 0:
        print("Assento Ocupado")
    else:
        print("Esgotado!")
        

