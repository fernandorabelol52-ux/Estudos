km = int(input("Qual será a distância percorrida em kilometros? "))

if km > 200:
    preço = km * 0.45
else:
    preço = km * 0.5

print(f"O preço da sua passagem será R${preço}")
