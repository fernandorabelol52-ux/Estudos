precos = [25.90, 10.50, 99.90, 45.00, 12.75]

final = len(precos)
while final >= 1:
    trocou = False 
    x = 0 
    
    while x < (final - 1): 

        if precos[x] < precos[x + 1]:
            trocou = True 
            temp = precos[x] 
            precos[x] = precos[x + 1] 
            precos[x + 1] = temp 
        x += 1 
    if not trocou: 
        break
    final -=1 

print("Preços em ordem decrescente:", precos)

for valor in precos:
    print(f"R${valor:.2f}")

#programa responde: 
#R$99.90
#R$45.00
#R$25.90
#R$12.75
#R$10.50