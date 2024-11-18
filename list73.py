def filtro_dicionario(dic, valor):
    return {k: v for k, v in dic.items() if v > valor}