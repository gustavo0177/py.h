def bubblesort(lista):
    for i in range(len(lista)- 1):
        for m in range (len(lista) -i -1):
            if lista[m] > lista[m +1]:
                lista[m], lista[m +1] = lista[m +1], lista[m]