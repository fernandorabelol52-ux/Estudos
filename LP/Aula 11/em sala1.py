precos = [25.90, 10.50, 99.90, 45.00, 12.75]

final = len(precos)
while final >= 1:
    trocou = False 
    x = 0 # serve para usarmos para caminhar pela lista, começando sempre do primeiro elemento (posição 0).
    
    while x < (final - 1): #loop que vai de "x = 0" ate "x = final - 1", pois evita de o programa comparar com um numero que não está na lista.

        if precos[x] > precos[x + 1]: #perguntando se o valor de trás e maior que o da frente.
            trocou = True # se a condição for verdadeira, precisamos inverter a posição deles. Assim se for falsa essa afirmação o programa encerra antecipadamente.
            temp = precos[x] #guardando o valor atual
            precos[x] = precos[x + 1] #pegando o valor da direita e colocando na esquerda.
            precos[x + 1] = temp #colocando o valor maior na direita.
        x += 1 #avançando na lista
    if not trocou: #otimização para encerrar antes se o "trocou = false".
        break
    final -=1 #diminuindo o tamanho da lista.

print("Preços em ordem decrescente:", precos)

for valor in precos:
    print(f"R${valor:.2f}")