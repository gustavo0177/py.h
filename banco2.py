saldo = 1000
senha = input("informa a senha:")
 
if senha == "1234":
 print("1.extrato")
print("2.deposito")
print("3.saque")
print("4.sair")
opcao = input("escolha uma opçao")

if opcao =="1":
 print(f"saldo:R${saldo:.2f}")
elif opcao =="2":
 valor=float(input("informe o valor do deposito"))
 saldo += valor
 print(f"voce depositou R${valor:.2f}.saldo atualizado:R${saldo:>2f}")
elif opcao =="3":
 valor= float(input("informe o valor do saque:R$"))
if valor <= saldo:
 saldo -= valor
 print(f"voce sacou:R${valor:.2f}.saldo atualizado:{saldo:.2f}")
else: 
 print("saldo insuficiente")
if senha!= senha:
  print("senha invalida")



 