def fibonacci(n):
    if n ==0:
        return 0
    elif n == 1:
        return 1
    
    anterior = 0 
    atual = 1
    contador = 2

    while contador <=n:
        proximo = anterior + atual
        anterior = atual
        atual = proximo
        contador +=1

    return atual