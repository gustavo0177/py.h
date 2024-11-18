def media_notas(dicionario):
    if not dicionario:
        return 0 
    soma = sum(dicionario.value())
    quantidade = len(dicionario)

    media = soma / quantidade
    return media