def apagar_vogais(s):
    vogais = "aeiouAEIOU"
    return ''.join([letra for letra in s if letra not in vogais])
print(apagar_vogais("ola mundo"))