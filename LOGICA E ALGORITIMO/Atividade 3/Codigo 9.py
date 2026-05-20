num = int(input("Digite um numero que será fatorado: "))
cont = num
resultado = 1

while cont > 1:
    resultado *= cont
    cont -= 1

print(f"O valor fatorado de {num} é: {resultado}")

