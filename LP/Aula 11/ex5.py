alunos = ["Carlos", "Ana", "Bruno", "Daniela", "Eduardo"]

cont = len(alunos)

while cont >= 1:
    trocou = False 
    i = 0
    
    while i < (cont - 1):
        if alunos[i] > alunos[i+1]:
            trocou = True 
            temp = alunos[i] 
            alunos[i] = alunos[i + 1] 
            alunos[i + 1] = temp
        i += 1 
    if not trocou: 
        break
    cont -=1 

print("Alunos em ordem alfabética:", alunos)

#programa responde:
#Alunos em ordem alfabética: ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo']
