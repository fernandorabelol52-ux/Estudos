lista_de_palavras = ["python", "java", "javascript", "csharp", "kotlin"]

numero = int(input("Digite um número: "))
indice = (numero * 776) % len(lista_de_palavras)
palavra = lista_de_palavras[indice].lower().strip()

for x in range(100):
    print()

digitadas = []
acertos = []
erros = 0

# Listas prontas com o desenho de cada linha, por quantidade de erros
cabeca = ["", "0 ", "0 ", "0 ", "0 ", "0 ", "0 "]
corpo   = ["", "",   " | ", " \\| ", " \\|/ ", " \\|/ ", " \\|/ "]
pernas  = ["", "",   "",    "",      "",       " / ",    "/ \\ "]
boneco = [cabeca, corpo, pernas]

while True:
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else "."
    print(senha)

    if senha == palavra:
        print("Você acertou!")
        break

    tentativa = input("\nDigite uma letra: ").lower().strip()

    if tentativa in digitadas:
        print("Você já tentou essa letra!")
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print("Você errou!")

    print("X==:==\nX : ")

    # Desenha cada linha do boneco buscando na lista, sem if/elif
    for linha in boneco:
        print(f"X{linha[erros]}")

    print("X\n================")

    if erros == 6:
        print("Enforcado!")
        break