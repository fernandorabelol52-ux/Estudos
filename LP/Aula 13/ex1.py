string1 = str(input("Digite a primeira string: "))
string2 = str(input("Digite a segunda string: "))

posicao = string1.find(string2)

if posicao != -1:
    print(f"A segunda string foi encontrada na posição {posicao}")
else:
    print("A segunda string não foi encontrada na primeira string")
