n = float(input("Digite o número para calcular a raiz quadrada: "))

b = 2.0

while True:
    p = (b + (n / b)) / 2
    quadrado_p = p * p
    
    diferenca = abs(n - quadrado_p)
    
    if diferenca < 0.0001:
        break
        
    b = p

print(f"A raiz quadrada aproximada de {n} é {p:2f}")
