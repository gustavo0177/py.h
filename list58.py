def conta_minusculas(texto):
    contador = 0

    for caracter in texto:
        if caracter.isupper():
            contador += 1

    return contador