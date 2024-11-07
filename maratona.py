#03) Questão

verde=int(input("Verde"))
ver=int(input("Vermelho"))
ama=int(input("Amarelo"))


if ver=="1" or "0":
    print(" Vermelho Está ligado")

elif ver=="0":
    print(" Vermelho está desligado")

elif ama=="1":
    print(" Amarelo está ligado")

elif ama=="0":
    print(" Amarelo está desligado")

elif verde=="1":
    print(" Verde está ligado")

elif verde=="0":
    print(" Verde está desligado")


#07) Questão 

while True:
    nome=str(input("Digite seu Login: "))
    senha=str(input("Digite sua senha:"))

    team_maiscula=False
    team_minusculo=False
    team_numero=False

    if len(senha) >=8:
        for caracter in senha:
            if caracter.isupper():
                team_maisculo:True
            elif caracter.islower():
                team_minusculo: True
            elif caracter.isdigit():
                team_numero: True

        if team_maiscula and team_minusculo and team_numero:
            print("Login válido")
            break
        else:
            print("Login inválido")


