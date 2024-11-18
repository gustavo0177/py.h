def substitui_texto_arquivo(nome_arquivo, palavra_antiga, palavra_nova):
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
    conteudo_novo = conteudo.replace(palavra_antiga, palavra_nova)
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(conteudo_novo)