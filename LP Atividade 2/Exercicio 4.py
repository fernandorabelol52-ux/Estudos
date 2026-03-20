salario = float(input("Qual é o valor do seu salário? "))

if salario > 1250:
    aumento = salario * 0.1
else:
    aumento = salario * 0.15

salario_calculado = aumento + salario

print(f"O valor do novo salrio será {salario_calculado} ")
