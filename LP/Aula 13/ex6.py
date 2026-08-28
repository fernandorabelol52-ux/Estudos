string1 = input("Insira a primeira string: ")
string2 = input("Insira a segunda string: ")
string3 = input("Insira a terceira string: ")

resultado = ""

for letra in string1:
    if letra in string2:
        posicao = string2.index(letra)
        resultado += string3[posicao]
    else: 
        resultado += letra

print(f"Resultado: {resultado}")
