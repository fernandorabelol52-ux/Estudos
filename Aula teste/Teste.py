while True: 
    pergunta = str(input("Vamos fazer listas?(sim/não) "))
    if pergunta == "sim":
        lista = []

        n1 = int(input("Quatos elementos tem na Lista 1? "))

        for i in range(n1):
            valor = int(input("Digite um numero para Lista 1: "))
            lista.append(valor)

        lista2 = []

        n2 = int(input("Quantos elementos tem na Lista 2? "))

        for i in range(n2):
            valor2 = int(input("Digite um numero para Lista 2: "))
            lista2.append(valor2)

        lista3 = sorted(set(lista + lista2))

        if lista3:
            media = sum(lista3) /  len(lista3)
            maior_valor = max(lista3)
            menor_valor = min(lista3)
        else:
            print("A lsita está fazia") 
        print(f"\n--- RESULTADO FINAL ----")
        print(f"Primeira Lista: {lista}")
        print(f"Segunda Lista: {lista2}")
        print(f"Terceira Lista: {lista3}")
        print(f"\nA Média dos valores da Lista 3 é {media:.2f}")
        print(f"O maior valor encontrado entre as duas Listas é {maior_valor}")
        print(f"O menor valor encontrado entre as duas Listas é {menor_valor}")
        print(f"A quantidade de numeros na Lista 3 é {len(lista3)}")
    else:
        print(" "*10 + "Até logo")
        break   





