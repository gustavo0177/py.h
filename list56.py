def gera_fibonacci_lista(n):
    if n == 0:
        return[]
    elif n == 1:
        return [0]
    
    fibonacci = [0,1]

    for i in range [2, n]:
        proximo = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(proximo)
    return fibonacci