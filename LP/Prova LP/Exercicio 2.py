num1 = int(input("Começa em: "))
num2 = int(input("Termina em: "))

soma = 0
atual = num1

while atual <= num2:
    if atual % 2 != 0:
        soma += atual
    atual += 1

print(f"A soma dos numeros impares no intervlo é: {soma}")
