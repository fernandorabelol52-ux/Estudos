preço_mercadoria = float(input("Digite o preço da mercadoria: "))
desconto = float(input("Digite o percentual de desconto: "))

calculo = preço_mercadoria * (desconto / 100)
descontando = preço_mercadoria - calculo

print ("O valor do desconto é ", calculo)
print ("O preço a pagar pela mercadoria é", descontando)

input("\nPressione Enter para sair...")