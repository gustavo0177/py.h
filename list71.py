def conta_elementos(lista):
    contagem={}
    for elemento in lista:
        contagem[elemento] =contagem.get(elemento, 0) +1
    return contagem