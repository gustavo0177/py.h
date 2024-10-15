n1= float(input("digite a sua primeira nota: "))
n2= float(input("digite a sua segunda nota: "))
n3= float(input("digite a sua terceria nota: "))
n4= float(input("digite a sua quarta nota: "))
media=(n1+n2+n3+n4)/4
if media == 10:
    print("aprovado com distinção")
elif media >=6:
    print("aprovado!")
else:
    print("reprovado")

