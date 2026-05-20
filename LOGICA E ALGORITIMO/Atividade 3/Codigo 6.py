
while True:
    start = str(input("Digite para iniciar (s/n): "))
    if start == "s":
        print("Programa iniciado...")
        print("-"*50)
        print()
        base = float(input("DIgite a Base: "))
        altura = float(input("DIgite a Altura: "))
        area = base * altura
        print(f"A area é de: {area:.2f}")
        print("-"*50)
        print()
    elif start == "n":
        print("Programa encerrado...")
        break
    else:
        print("Valor invalido!")
        continue
