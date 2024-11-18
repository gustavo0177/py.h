def conta_ocorrencias_caracteres(s):
    ocorrencias = {}

    for caracter in s:
        if caracter in ocorrencias:
            ocorrencias[caracter] +=1
        else:
            ocorrencias[caracter]= 1
    return ocorrencias