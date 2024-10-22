
while True:
    total_c = 0
    cliente =  int(input("1-cliente\n0-sair"))
    if cliente ==1:
       while True:
           preco =  float(input(" digite o preco do produto ou digite 0 para finalizar a compra: "))
           if preco == 0:
              break
           nome_p = str(input("nome do produto: "))
           total_c += preco
           print(f"{nome_p}: {preco}")
       print(f"total: {total_c}")
   
       while True:
           pagamento = float(input(" digite o valor que voce pagara"))
           if pagamento < total_c:
                print("valor insuficiente da compra")
           else:
               troco = pagamento - total_c
               print(troco)
               break
    elif cliente==0:
      break
    
  

 
      

