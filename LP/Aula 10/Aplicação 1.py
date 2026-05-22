V = int(input("Quais os numeros que compoe a Lista V: "))
P = []
I = []

for i in V:
    if i % 2 == 0:
        P.append(i)
    else:
        I.append(i)

print("Numeros Pares: ",P)
print("Numeros Impares: ",I)

