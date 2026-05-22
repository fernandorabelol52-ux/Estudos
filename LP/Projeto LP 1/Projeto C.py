produtos = []

while True:
    #inserindo os dados do produto a ser calculado para obter o lucro
    nome_produto = str(input("\nDigite o nome do produto (Digite 'sair' para finalizar): "))
    
    #condição de parada
    if nome_produto.lower() == "sair":
        break

    preço_produto = float(input("Digite o preço para produzir o produto: "))
    preço_venda = float(input("Digite o preço de venda do produto: "))
    quantidade_produzida = int(input("Digite a quantidade produzida do produto: "))
    quantidade_vendida = int(input("Digite a quantidade vendida do produto: "))

    #calculo do faturamento
    custo_produto = preço_produto * quantidade_produzida
    receita = preço_venda * quantidade_vendida
    lucro = receita - custo_produto

    # Armazenando os dados na lista em vez de imprimir agora
    produtos.append({
        "nome": nome_produto,
        "custo": custo_produto,
        "receita": receita,
        "lucro": lucro
    })
    
    # Opcional: Feedback simples para o usuário
    print(f"     Produto '{nome_produto}' cadastrado.")

# Após encerrar o programa, mostrar tudo
if produtos:
    print("\n     RESUMO DOS PRODUTOS CADASTRADOS\n")
    
    produto_maior_lucro = produtos[0]
    
    for p in produtos:
        # Verifica quem teve o maior lucro
        if float(p["lucro"]) > float(produto_maior_lucro["lucro"]):
            produto_maior_lucro = p
            
        # Imprime os resultados individuais
        print(f"\nProduto: {p['nome']}")
        print(f"Faturamento: R${p['receita']:.2f}")
        print(f"Custo: R${p['custo']:.2f}")
        
        if float(p["lucro"]) > 0:
            print(f"Resultado: LUCRO de R${p['lucro']:.2f}")
        elif float(p["lucro"]) < 0:
            print(f"Resultado: PREJUÍZO de R${abs(p['lucro']):.2f}")
        else:
            print("Resultado: ZERO A ZERO (sem lucro ou prejuízo)")
        
    print("\n")
    
    # Mostra o produto mais lucrativo
    if float(produto_maior_lucro["lucro"]) > 0:
        print(f"O produto mais lucrativo foi '{produto_maior_lucro['nome']}' com um lucro de R${produto_maior_lucro['lucro']:.2f}.")
    else:
        print(f"Nenhum produto gerou lucro positivo. O melhor resultado (ou menor prejuízo) foi de '{produto_maior_lucro['nome']}'.")
else:
    print("\nNenhum produto foi cadastrado.")

    