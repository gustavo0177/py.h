def a(x):
    if x>0:
        return "P"
    elif x<0:
        return "N"
    else:
        return "o valor iguala zero!!"

while True:
    num = int(input("digite um numero: "))
    if a (num)== "N":
       print("negativo")
    elif a (num)== "P":
       print("positivo")
    else:
      print(a(num))