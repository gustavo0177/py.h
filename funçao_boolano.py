def par(x):
    if (x%2)==0:
        return True
    else:
        return False
    
while True:
    num = int(input("insira o numero"))
    if par (num):
       print("E par")
    else:
      print("e impar")