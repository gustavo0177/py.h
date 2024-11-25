

class Pessoa:
    def __init__(self, nome, altura):
        self.nome = nome
        self.altura = altura

    def verificar_altura(self):
        if self.altura > 1.75:
            print(f"{self.nome} é mais alto(a) que 1,75 m.")
        else:
            print(f"{self.nome} não é mais alto(a) que 1,75 m.")

pessoa = Pessoa("Carlos", 1.80)
pessoa.verificar_altura()