quantidade = int(input("Digite a quantidade de números primos que deseja imprimir: "))

contador = 0
num = 2  # Este é o número que vamos testar se é primo ou não

while contador < quantidade:
    divisor = 2
    while divisor < num:
        if num % divisor == 0:
            break
        divisor += 1
    else:
        print(num)
        contador += 1
    num += 1
