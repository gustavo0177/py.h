def elementos_unico(lista):
    return[x for x in lista if lista.count(x) == 1]

print(elementos_unico([1,2,3,2,4]))