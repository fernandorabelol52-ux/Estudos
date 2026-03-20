divida = float(input("Valor da divida: "))
taxa = float(input("Juros: "))
pagamento = float(input("Pagamento mensal: "))

if (divida * (taxa / 100)) >= pagamento:
    print("Erro")
else:
    total_pago: 0
    total_juros: 0
    meses = 0

    while divida > 0:
        juros_do_mes = divida * (taxa / 100)
        total_juros += juros_do_mes
        divida += juros_do_mes
        
        if divida > pagamento:
            divida -= pagamento
            total_pago += pagamento
        else:
            total_pago += divida
            divida = 0
        meses += 1
print(f"Quantidade de meses: {meses}")
print(f"Total pago: R$ {total_pago:.2f}")
print(f"Total de juros pagos: R$ {total_juros:.2f}")