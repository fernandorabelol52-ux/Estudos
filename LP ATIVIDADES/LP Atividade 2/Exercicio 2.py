km = int(input("Qual é a velocidade que o carro esta? "))

if km>80:
	conta= km - 80
	conta2= conta * 5
	print(f"Seu carro foi multado em R${conta2}") 
else:
	print("Seu carro não foi multado")

input("\nPressione Enter para sair...")
 