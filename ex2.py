populacao_a = 80000
populacao_b = 200000
taxa_crecimentoA = 0.03
taxa_crecimentoB = 0.015
ano = 0
while populacao_a < populacao_b:
    populacao_a += populacao_a * taxa_crecimentoA
    populacao_b += populacao_b * taxa_crecimentoB
    ano += 1

print(f" e necessario {ano} para a populacao A passar B")