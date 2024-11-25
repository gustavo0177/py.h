class bichinhovirtual:
    def __init__(self,nome,fome,saude,idade):
       self.nome = nome
       self.fome = fome
       self.saude = saude
       self.idade = idade
    
    def alterar(self,alterar_nome,alterar_idade,alterar_saude,alterar_fome):
        self.alterar_nome = alterar_nome
        self.alterar_idade = alterar_idade
        self.alterar_saude = alterar_saude
        self.alterar_fome = alterar_fome
    
    def humor(self,humor_alegre,humor_normal,humor_triste):
        self.humor_alegre = humor_alegre
        self.humor_normal = humor_normal
        self.humor_triste = humor_triste
    
    def saude(self,saude_alta,saude_media,saude_baixa):
        self.saude_alta = saude_alta
        self.saude_media = saude_media
        self.saude_baixa = saude_baixa
    
    def retornar(self,retornar_nome,retornar_fome,retornar_saude,retornar_idade):
        self.retornar_nome =  retornar_nome
        self.retornar_fome = retornar_fome
        self.retornar_saude = retornar_saude
        self.retornar_idade = retornar_idade
    
    def calcular_humor(self):
        return (self.fome + self.saude) / 2
    
    