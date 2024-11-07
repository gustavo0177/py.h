while True:
    n = str(input("DIGITE SEU NOME"))
    if len(n) < 3:
        print("nome invalido. tente novamente")
    else:
        print("nome valido")
        break
while True:
        idade = int(input("digite a sua idade"))
        if idade > 0 and idade <= 150:
            print("idade valida")
            break
        else:
            print("idade invalida")
while True:
     sal = float(input("digite seu salario"))      
     if sal <0:
          print("salario invalido")
     else:
          print("salario valido")
          break
     while True:
          sexo = str(input("digite o sexo F M ou O:").upper())
          if sexo == "F" or sexo == "M" or sexo == "O":
           print("sexo valido")
           break
          else:
              print("sexo invalido .tente novamete")
while True:
    civil = str(input("digite o seu estado civil  S ,C ,V ,D").upper())
    if civil == "S" or civil== "C" or civil== "V" or civil== "D":
        print("estado civil vali8do ")
        break
    else:
         print("estado civil invalido")

          