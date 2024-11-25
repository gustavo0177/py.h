import pydantic
from pydantic import BaseModel
class Usuario(BaseModel):
    nome: str
    idade: int
    sexo: str
usuario = Usuario(nome="gustavo",idade=17,sexo="masculino")
print(usuario.nome)
print(usuario.idade)
print(usuario.sexo)