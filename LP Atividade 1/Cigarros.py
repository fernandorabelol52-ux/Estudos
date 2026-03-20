cigarros_por_dia = int(input("Quantos cigarros você fuma por dia? "))
anos_fumando = int(input("Por quantos anos você é fumante? "))

calculo = cigarros_por_dia * 365 * anos_fumando * 10 / 3600

print ("A quantidade de vida perdida é", calculo, "dias")

input("\nPressione Enter para sair...")