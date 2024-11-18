from functools import reduce
def mcd(a,b ):
    if b == 0:
        return  a
    else:
        return mcd(b, a %b)
    
def mdc_lista(lista):
    if not lista:
        return None
    elif len(lista) == 1:
        return lista[0]
    else:
        return reduce(mcd, lista)