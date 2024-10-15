p1 = str(input(" vc telefonou para vitima, coloque S para sim e N para nao: "))
p2 = str(input("vc esteve mp local do crime, coloque S para sim e N para nao: "))
p3 = str(input("vc mora perto da vitima, coloque S para sim e N para nao: "))
p4 = str(input(" vc devia para vitima, coloque S para sim e N para nao: "))
p5= str(input(" vc ja trabalhou para vitima, coloque S para sim e N para nao: "))
cont=0
if p1.upper() =="S":
    cont=cont+1

if p2.upper()=="S":
    cont=cont+1

if p3.upper() =="S":
    cont=cont+1

if p4.upper()=="S":
    cont=cont+1

if p5.upper()=="S":
    cont=cont+1



if cont==5:
    print("assasino")
elif cont >=3 and cont <4:
    print("complice")
elif cont ==2:
    print("suspeita")
elif cont<2:
    print("inocente")

    