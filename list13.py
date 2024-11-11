def capitalizar(texto):
    return ''.join([capitalizar() for palavra in texto.split()])
print(capitalizar("ola mundo como vc estar"))