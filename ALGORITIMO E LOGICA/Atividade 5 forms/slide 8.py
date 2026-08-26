ready = str(input("Quer calcular a nota do aluno?(S/N)"))

if ready.upper() == "s":
    soma = 0
    for i in range(9):
        notas = float(input(f"Nota {i}:"))
        soma += notas
    media = notas / 10 
    print(f"A nota final do aluno é {media}")

elif ready.upper() == "n":
    print("Não vamos calcular")
else:
    print("Responda uma das opções(S/N)")
