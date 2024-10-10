senha=input("informe a senha")

if senha == "1234":
 print("1.extrato")
print("2.deposito")
print("3.saque")
print("4.sair")
opcao = input("escolha uma opçao")

if opcao == "1":
 print("saldo: R$ 1000")

elif opcao == "2":
 valor = input("o valor do deposito:R$") 
 print(f"voce depositou R${valor}")

elif opcao == "3":
 valor = input("o valor do saque:R$")
print(f"voce sacou R${valor}")

if opcao == "4":
 print("saindo..")

else:
 print("opçao invalida")



