
def merge_dicionarios(d1, d2):
    resultado = d1.copy()
    for chave, valor in d2.items():
        resultado[chave] = resultado.get(chave, 0) + valor
    return resultado