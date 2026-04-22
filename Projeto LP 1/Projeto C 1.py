while True:
    nome_produto = str(input("\nNome do Produto (Digite 'sair' para finalizar): "))

    if nome_produto.lower() == "sair":
        break
    
    preço_produto = float(input("\nPreço de fabricação do Produto: "))
    preço_venda = float(input("Preço de venda do Produto: "))
    quantidade_produzida = int(input("Quantidade do Produto produzida: "))
    quantidade_vendida = int(input("Quntidade do Produto vendida: "))

    custo_produto = preço_produto * quantidade_produzida
    receita = preço_venda * quantidade_vendida
    lucro = receita - custo_produto

    print(f"\nProduto: {nome_produto}")
    print(f"Faturamento: R${receita:.2f}")
    print(f"Custo: R${custo_produto:.2f}")
    
    if lucro > 0:
        print(f"\nO Produto de um lucro de R${lucro:.2f}")
    elif lucro < 0:
        print(f"O Produto deu um prejuizo de R${abs(lucro):.2f}")
    else:
        print("O Produto se pagou, porém não deu lucro")
