ready = str(input("Quer calcular a nota do aluno?(S/N)"))

if ready.upper() == "s":
    nota1 = float(input("Nota 1:"))
    nota2 = float(input("Nota 2:"))
    nota3 = float(input("Nota 3:"))
    nota4 = float(input("Nota 4:"))
    nota5 = float(input("Nota 5:"))
    nota6 = float(input("Nota 6:"))
    nota7 = float(input("Nota 7:"))
    nota8 = float(input("Nota 8:"))
    nota9 = float(input("Nota 9:"))
    nota10 = float(input("Nota 10:"))
    soma = nota1 + nota2 + nota3 + nota4 + nota5 + nota6 + nota7 + nota8 + nota9 + nota10
    media = soma / 10
    print(f"A media do aluno é {media}")

elif ready.upper() == "n":
    print("Não vamos calcular")
else:
    print("Responda uma das opções(S/N)")
