string = input("Insira a string: ")
contagem = {}

for letra in string:
    if letra in contagem:
        contagem[letra] += 1
    else: 
        contagem = 1

for letra in contagem:
    print(f"{letra}: {contagem[letra]}")