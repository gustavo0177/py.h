def conta_palavras_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
        palavras = conteudo.split()
        return len(palavras)