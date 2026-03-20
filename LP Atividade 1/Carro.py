dias_alugados = int(input("Por quantos dias o carro foi alugado? "))
kms_rodados = float(input("Neste tempo o carro percorreu quantos quilômetros? "))

calculo = dias_alugados * 60
calculo2 = kms_rodados * 0.15
calculo3 = calculo + calculo2

print ("O valor a pagar pelo aluguel do carro é de", calculo3, "reais")

input("\nPressione Enter para sair...")