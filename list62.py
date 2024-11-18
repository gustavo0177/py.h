def valida_senha(senha):
    
    if len(senha) < 9:
        return False

    
    caracteres_especiais = "!@#$%^&*()-_+=<>?/|\\{}[]~"
    tem_caracter_especial = any(char in caracteres_especiais for char in senha)

    
    tem_maiuscula = any(char.isupper() for char in senha)
    tem_minuscula = any(char.islower() for char in senha)

   
    tem_numero = any(char.isdigit() for char in senha)

    
    if tem_caracter_especial and tem_maiuscula and tem_minuscula and tem_numero:
        return True
    else:
        return False