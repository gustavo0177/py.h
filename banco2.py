import os
class Conta():
    def __init__(self,saldo,cpf: str,nome,senha: str):
        self.__saldo=saldo
        self.__cpf=cpf
        self.nome=nome
        self.__senha=senha
    def extrato(self):
        senha=input('insira sua senha\n')
        os.system('cls')
        if senha==self.__senha:
            print(f'nome: {self.nome}\ncpf: {self.__cpf}\nsaldo em conta: {self.__saldo}')
        else:
            print('senha inválida')
    def depositar(self,valor):
        self.__saldo +=valor
        return self.__saldo
    def sacar(self,valor):
        self.__saldo-=valor
        return self.__saldo
    def entrar(self):
        while True:
            senha=input('insira sua senha\n')
            if senha==self.__senha:
                os.system('cls')
                break
            else:
                print('senha inválida')
                os.system('pause')
                os.system('cls')
                continue
            
conta=Conta(0,312312323,'gustavo','5')
Conta.entrar(conta)

while True:
    test=int(input('1-Extrato\n2-Deposito\n3-Saque\n0-Sair\n'))
    os.system('cls')
    if test==1:
        Conta.extrato(conta)
        os.system('pause')
        os.system('cls')
    elif test==2:
        x=int(input('valor do deposito: '))
        Conta.depositar(conta,x)
        print('deposito feito com sucesso!')
        os.system('pause')
        os.system('cls')
    elif test==3:
        x=int(input('valor do saque: '))
        Conta.sacar(conta,x)
        print('saque feito com sucesso!')
        os.system('pause')
        os.system('cls')
    elif test==0:
        print('encerrado')
        break