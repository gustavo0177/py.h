try:
 
 a = int(input("digite uma palavra "))
except ValueError:
 print("digite apenas numeros ")
except:
 print("erro desconhecido")