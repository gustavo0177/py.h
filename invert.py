def inverte(nome,sobrenome):
    nomeinverso= sobrenome+","+nome
    return nomeinverso
nome = input("nome: ")
sobrenome = input("sobrenome: ")
invertido = inverte(nome,sobrenome)
print("ola",invertido)