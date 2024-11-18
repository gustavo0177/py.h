import random
def gerar_senha(tamanho):
    caracter ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+<>?"
    senha = "".join(random.choice(caracter) for _ in range(tamanho))

    return senha 