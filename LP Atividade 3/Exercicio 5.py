deposito = int(input("Digite o valor do deposito: "))
juros = float(input("Digite a taxa de juros da poupanca: "))

final = deposito
mes = 0

while True:
    if mes <= 24:
        final = final + (final * (juros / 100))
        print(f"{mes} - {final:.2}")
        mes = mes + 1
    else:
       calculo = final - deposito
       break
print(f"O valor ganho no final dos 24 meses foram de {calculo}")




