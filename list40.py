def mediana(lista):
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    if n % 2==1:
        return lista_ordenada[n//2]
    else:
        meio1 = lista_ordenada[n // 2 -1]
        meio2 = lista_ordenada[n // 2]
        return(meio1 + meio2) /2