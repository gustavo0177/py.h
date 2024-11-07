while True:
    usuario = str(input("digite o usuario "))
    senha = str(input("digite a senha"))
    if senha == usuario:
        print("senha invalida . tente novamnete")
    else:
        print("comfirmado")