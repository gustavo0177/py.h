class ContaBancaria:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depositado: R$ {valor}. Saldo atual: R$ {self.saldo}")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Sacado: R$ {valor}. Saldo atual: R$ {self.saldo}")
        else:
            print("Saldo insuficiente.")


conta = ContaBancaria(100)
conta.depositar(50)
conta.sacar(30)
conta.sacar(150)
class ContaBancaria:
    def __init__(self, saldo=0):
        self.saldo = saldo

class Banco:
    def __init__(self):
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def listar_saldos(self):
        for i, conta in enumerate(self.contas):
            print(f"Conta {i + 1}: R$ {conta.saldo:.2f}")

conta1 = ContaBancaria(100)
conta2 = ContaBancaria(200)
banco = Banco()
banco.adicionar_conta(conta1)
banco.adicionar_conta(conta2)
banco.listar_saldos() 