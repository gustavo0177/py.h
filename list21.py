def midia_lista(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)


print(midia_lista([1,2,3,4,5,]))