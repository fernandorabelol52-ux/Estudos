numero1 = int(input("Me fale o Numero 1: "))
numero2 = int(input("Me fale o Numero 2: "))
operação = str(input("Qual será a operação? "))

if operação == "soma":
    calculo = numero1 + numero2
if operação == "subtração":
    calculo = numero1 - numero2
if operação == "multiplicação":
    calculo = numero1 * numero2
if operação == "divisão":
    calculo = numero1 / numero2

print(f"O resultado do calculo é {calculo}")
