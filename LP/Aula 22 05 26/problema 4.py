lojas = ["L1", "L2", "L3", "L4"]
demandas = [50, 80, 40, 100]
portos = ["P1", "P2", "P3"]

distancias = [
    [30, 20, 24, 18],
    [12, 36, 30, 24],
    [8,  15, 25, 20]
]

capacidade_caminhao = 10

total_distancia_ida = 0
total_distancia_ida_volta = 0

print("==================================================")
print("          PLANO DE TRANSPORTE OTIMIZADO           ")
print("==================================================")
print()

for j in range(len(lojas)):
    loja = lojas[j]
    demanda = demandas[j]
    
    viagens = demanda // capacidade_caminhao
    if demanda % capacidade_caminhao != 0:
        viagens += 1
        
    menor_distancia = distancias[0][j]
    melhor_porto = portos[0]
    
    for i in range(1, len(portos)):
        distancia_atual = distancias[i][j]
        if distancia_atual < menor_distancia:
            menor_distancia = distancia_atual
            melhor_porto = portos[i]
            
    distancia_loja_ida = viagens * menor_distancia
    distancia_loja_ida_volta = viagens * menor_distancia * 2
    
    total_distancia_ida += distancia_loja_ida
    total_distancia_ida_volta += distancia_loja_ida_volta
    
    print(f"Loja: {loja}")
    print(f"  - Demanda total: {demanda} m³")
    print(f"  - Melhor ponto de abastecimento: {melhor_porto} (distância de {menor_distancia} km)")
    print(f"  - Número de viagens necessárias: {viagens} viagens (capacidade de {capacidade_caminhao} m³ por viagem)")
    print(f"  - Distância percorrida para esta loja:")
    print(f"    * Apenas ida: {distancia_loja_ida} km")
    print(f"    * Ida e volta (retorno ao porto): {distancia_loja_ida_volta} km")
    print("-" * 50)

print()
print("==================================================")
print("                   RESUMO TOTAL                   ")
print("==================================================")
print(f"Distância total percorrida (apenas ida): {total_distancia_ida} km")
print(f"Distância total percorrida (ida e volta): {total_distancia_ida_volta} km")
print("==================================================")
