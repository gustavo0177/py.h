def conta_consoantes(texto):
    
    consoantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    
    
    contador = 0

   
    for char in texto:
        if char in consoantes:
            contador += 1

    return contador


texto_teste = " um texto"
conta_consoantes(texto_teste)
