contador = 0
soma = 0

while contador < 5:
    nota = float(input("Digite a nota do aluno:"))
    soma += nota
    contador += 1
media = soma / 5
print("A media das notas é: ", media)