def soma_diagonal(matriz):
    n = len(matriz)
    soma = 0

    for i in range(n):
        soma += matriz[i][i]
        soma += matriz[i][n - 1 -i]

    if n % 2 == 1:
        meio = n //2 
        soma -+ matriz[meio] [meio]
    return soma