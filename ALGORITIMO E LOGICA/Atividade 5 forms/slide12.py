vet = []

for i in range(5):
    valor = int(input(f"Valor {i + 1}: "))
    vet.append(valor)

print("Inverso: ", end=" ")
for i in range(4, -1, -1):
    print(vet[i], end=" ")
print()

print("Quadrado de cada valor:")
for i in range(5):
    print(vet[i]*vet[i], end=" ")
print()

print("Maiores que 3: ")
for i in range(5):
    if vet[i] > 3:
        print(vet[i], end=" ")
print()

print("Pares: ")
for i in range(5):
    if vet[1] % 2 == 0:
        print(vet[i], end=" ")
print()
    

