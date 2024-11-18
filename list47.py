def conta_ocoreencia_recursivas(lista, elem):
    if not lista:
        return 0
    else:
        return(1 if lista[0] == elem else 0 ) + conta_ocoreencia_recursivas(lista[1:], elem)