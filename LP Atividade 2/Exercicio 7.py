valor_casa = float(input("Qual é o vaolr da casa que será comprada? "))
salario = float(input("Qual é o seu salario? "))
anos_a_pagar = float(input("Por quantos anos vai ser paga a casa? "))

parcelas = valor_casa / anos_a_pagar
salario_porcentagem = salario * 0.30

if salario_porcentagem < parcelas:
    print("Não erá possivel fazer o emprestimo")
else:
    print(f"O valor das prestações será de {parcelas} por {anos_a_pagar} anos")