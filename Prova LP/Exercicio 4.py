populacaoA = 80000
taxaA = 0.04
populacaoB = 200000
taxaB = 0.015
ano = 0

while populacaoA < populacaoB:
    populacaoA += populacaoA * taxaA
    populacaoB += populacaoB * taxaB
    ano += 1
print(f"Anos necessarios: {ano}")
print(f"Popullação final da Cidade A: {populacaoA}")
print(f"População final da Cidade B: {populacaoB}")
