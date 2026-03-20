#inserindo os dados do produto a ser calculado para obter o lucro
nome_produto = str(input("Digite o nome do produto: "))
preço_produto = float(input("Digite o preço para produzir o produto: "))
preço_venda = float(input("Digite o preço de venda do produto: "))
quantidade_produzida = int(input("Digite a quantidade produzida do produto: "))
quantidade_vendida = int(input("Digite a quantidade vendida do produto: "))

#calculo do faturamento
custo_produto = preço_produto * quantidade_produzida
receita = preço_venda * quantidade_vendida
lucro = receita - custo_produto

print(f"O faturamento foi de R${receita:.2f}")
print(f"O custo foi de R${custo_produto:.2f}")
print(f"O lucro foi de R${lucro:.2f}")