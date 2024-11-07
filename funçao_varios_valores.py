def cadastro():
    name =  input("qual e os eu nome: ")
    age = int(input("idade: "))
    return name,age
print("iniciando cadastro...")
nome,idade = cadastro()
print("cadastro realizado com sucesso..")
print("seu nome é",nome,"e vc tem",idade,"anos de idade")