kwh_cliente = float(input("Qual é a quantidade de kWh que é consumida? "))
tipo_instalação = str(input("Qual é o tipo da instalação que foi utilizada? "))

if tipo_instalação == "R":
    if kwh_cliente > 500:
        conta = kwh_cliente * 0.65
    else:
        conta = kwh_cliente * 0.4
if tipo_instalação == "C":
    if kwh_cliente > 1000:
        conta = kwh_cliente * 0.6
    else:
        conta = kwh_cliente * 0.55
if tipo_instalação == "I":
    if kwh_cliente > 5000:
        conta = kwh_cliente * 0.60
    else:
        conta = kwh_cliente * 0,55

print(f"O valor a pagar pela energia consumida é R${conta}")
