total = 0

while True:
    codigo = int(input("Digite o codigo do produto (ou pressione 0 para sair): "))
    

    if codigo == 0:
        break
    if codigo == 1:
        preço = 0.5 
    elif codigo == 2:
        preço = 1.0    
    elif codigo == 3:
        preço = 4.0      
    elif codigo == 4:
        preço = 7.0
    elif codigo == 5:
        preço = 8.0
    else:
        print("Codigo invalido!")
    quantidade = int(input("Qual é a quantidade comprada: "))
    total = total + (quantidade * preço)



print(f"\nTotal da compra: R${total:.2f}")
