def troca_vogais(s,nova_vogais):
    vogais = "aeiouAEIOU"
    return ''.join([nova_vogais if letra in vogais else letra  in s])
print(troca_vogais("ola mundo"))