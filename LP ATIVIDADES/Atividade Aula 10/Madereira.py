total_tabuas = 400
total_horas = 450

lucro_cadeira = 180
lucro_mesa = 320

tabuas_por_cadeira = 5
horas_por_cadeira = 10

tabuas_por_mesa = 20
horas_por_mesa = 15


max_lucro = 0
melhor_qtd_cadeiras = 0
melhor_qtd_mesas = 0

max_cadeiras_possiveis = total_horas // horas_por_cadeira  
max_mesas_possiveis = total_tabuas // tabuas_por_mesa      


for cadeiras in range(max_cadeiras_possiveis + 1):
    for mesas in range(max_mesas_possiveis + 1):
        
        tabuas_gastas = (cadeiras * tabuas_por_cadeira) + (mesas * tabuas_por_mesa)
        horas_gastas = (cadeiras * horas_por_cadeira) + (mesas * horas_por_mesa)
        
       
        if tabuas_gastas <= total_tabuas and horas_gastas <= total_horas:
            lucro_atual = (cadeiras * lucro_cadeira) + (mesas * lucro_mesa)
            
            if lucro_atual > max_lucro:
                max_lucro = lucro_atual
                melhor_qtd_cadeiras = cadeiras
                melhor_qtd_mesas = mesas

print("--- RESULTADO DA FÁBRICA ---")
print(f"Para obter o LUCRO MÁXIMO de R$ {max_lucro:.2f}, construa:")
print(f"-> {melhor_qtd_cadeiras} Cadeiras")
print(f"-> {melhor_qtd_mesas} Mesas")
