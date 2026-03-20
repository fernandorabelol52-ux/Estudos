dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Digite o divisor: "))

quociente = 0
resto = dividendo

while True:
    if divisor == 0:
        print("Não é possivelser zero")
    if resto >= divisor:
        resto = resto - divisor
        quociente = quociente + 1 
    else:
        break
print(f"Quociente: {quociente}")
print(f"Resto: {resto}")

