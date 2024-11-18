def multiplica_escalar(lista, escalar):
    return [x * escalar for x in lista]
lista = [1, 2, 3, 4]

escalar = 3
resultado = multiplica_escalar(lista,escalar)
print(resultado)