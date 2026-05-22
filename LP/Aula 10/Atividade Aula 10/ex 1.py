numeros = [45, 12, 89, 4, 33, 7, 102, 1]

# Assumimos que o primeiro número da lista é o menor de todos para começar a comparação
menor_numero = numeros[0]

# O laço 'for' vai passar por cada número dentro da lista
for numero in numeros:
    
    # Se o número que o 'for' está olhando agora for menor que o nosso "menor_numero" atual...
    if numero < menor_numero:
        # ...nós atualizamos a variável para guardar esse novo número que é menor
        menor_numero = numero

print(f"Lista de números: {numeros}")
print(f"O menor número da lista é: {menor_numero}")
