def conta_vogais(texto):
    vogais = "aeiouAEIOU"
    contador = 0
    for caractere in texto:
        if caractere in vogais:
            contador += 1
            return contador
        
print(conta_vogais("ola muuuundo!!"))
print(conta_vogais("Python!"))