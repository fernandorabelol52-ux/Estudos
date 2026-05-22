num = int(input("Digite um número: "))

if num <= 1:
    print("Não é primo")
else:
    divisor = 2
    while divisor < num:
        if num % divisor == 0:
            print("Não é primo")
            break
        divisor += 1
    else:
        print("É primo")