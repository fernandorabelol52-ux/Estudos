num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

resultado = 0
contador = 0

while True:
    if num2 == 0:
        print("0")
    resultado = resultado + num1
    contador = contador + 1
    if contador == num2:
        break
print(f"O resultado da multiplicação é {resultado}")
