def raiz_quadrada(n):

    if n < 0 :
        return None
    aproximacao = n / 2
    for _ in range(20):
        aproximacao = (aproximacao + n / aproximacao) / 2 
    return aproximacao