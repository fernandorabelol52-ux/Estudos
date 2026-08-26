vet1 = []
vet2 = []

while True:
    ready = str(input("Vamos começar?(S/N) "))

if ready.upper() == "s":
    for i in range(5):
        valor = int(input(f"vet1: pos {i + 1}: "))
        vet1.append(valor)

    for i in range(5):
        valor = int(input(f"vet2: pos {i + 1}: "))
        vet2.append(valor)

    print("soma: ")
    for i in range(5):
        print(vet1[i] + vet2[i], end=" ")   

elif ready.upper() == "n":
    print("Não vamos calcular")
else:
    print("Responda uma das opções(S/N)")