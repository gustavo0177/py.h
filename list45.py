def somatorio_lista_recursivo(lista):
    if not lista:
        return 0
    else:
        return lista[0] + somatorio_lista_recursivo(lista[1:1])
    