n1= float(input("digite a sua primeira nota: "))
n2= float(input("digite a sua segunda nota: "))
n3= float(input("digite a sua terceria nota: "))
n4= float(input("digite a sua quarta nota: "))
media=(n1+n2+n3+n4)/4
if media >= 9.1 and media<=10:
    print(f"vc foi aprovado a sua nota foi {media} O conceito foi A")
elif media >=7 and media <=9:
     print(f"vc foi aprovado a sua nota foi {media} O conceito foi B")
elif media >=6.0 and media <=7.5:
     print(f"vc foi aprovado a sua nota foi {media} O conceito foi C")     
elif media >=4.1 and media <=5.9:
     print(f"vc foi Reprovado a sua nota foi {media} O conceito foi D")
elif media >=0 and media <=4.0:
     print(f"vc foi Reprovado a sua nota foi {media} O conceito foi E")

