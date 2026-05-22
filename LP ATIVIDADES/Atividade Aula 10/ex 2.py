T = [-10, -8, 0, 1, 2, 5, -2, -4]

menor_temp = T[0]
maior_temp = T[0]

for temp in T:
    if temp < menor_temp:
        menor_temp = temp
    if temp > maior_temp:
        maior_temp = temp

media = sum(T) / len(T)

print(f"A maior temperatura foi: {maior_temp}")
print(f"A menor temperatura foi: {menor_temp}")
print(f"A média de temperatura foi: {media}")



