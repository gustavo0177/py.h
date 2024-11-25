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

