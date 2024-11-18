def conta_linhas(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        return len(arquivo.readlines())