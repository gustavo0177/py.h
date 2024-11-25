
class bola:
 
  def __init__(self,cor,circuferencia,material):
    self.cor = cor
    self.circuferencia = circuferencia
    self. material = material
  def troca_cor(self, cor2):
    self.cor = cor2
  def mostra_cor(self):
    return self.cor
  
  bola =bola ("roxo",20,"couro")




class quadrado:
    def __init__(self,tamanho_ld):
        self.tamanho_ld = tamanho_ld
    def mudar_valor_lado(self,novo_tamanho):
        self.tamanho_ld = novo_tamanho
    def mudar_valor_lado(self):
        return self.tamanho_ld 
    def mudar_area(self):
        return self.tamanho_ld
    
Quadrado = quadrado(4)
print(f"tamanho inicial: {Quadrado.mudar_valor_lado()}")
print(f"area inicial: {Quadrado.mudar_area()}")

Quadrado.mudar_valor_lado(6)
print(f"novo tamanho do lado {Quadrado.mudar_valor_lado()}")
print(f"nova area: {Quadrado.mudar_area()}")








class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")


pessoa = Pessoa("Ana", 25)
pessoa.exibir_informacoes()


    