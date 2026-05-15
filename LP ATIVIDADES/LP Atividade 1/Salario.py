salario = float(input("Digite o valor do salario: "))
porcentagem = float(input("Digite a porcentagem de aumento: "))

valor_aumento = salario * (porcentagem / 100)
novo_salario = salario + valor_aumento

print ("O valor do aumento é: ", valor_aumento)
print ("O novo salario é: ", novo_salario)

input("\nPressione Enter para sair...")
