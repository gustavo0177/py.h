salario_atual = float(input("digite o seu salario: "))

if salario_atual <= 280:
 aumento= salario_atual * 0.20
 salariototal=salario_atual+aumento
 print(f" o seu salario atuel e de {salario_atual} teve um almento so seu salario foi para: {salariototal}")

elif salario_atual >280 and salario_atual <=700:
 aumento= salario_atual * 0.15
 salariototal=salario_atual+aumento
 print(f"o seu salaraio atual e de {salario_atual} teve um almento o seu salario foi para:{salariototal}")

elif salario_atual >700 and salario_atual <=1500:
 aumento= salario_atual * 0.10
 salariototal=salario_atual+aumento
 print(f"o seu salaraio atual e de {salario_atual} teve um almento o seu salario foi para: {salariototal}")
else:
  salario_atual>= 1500
  aumento=salario_atual* 0.05
  salariototal=salario_atual+aumento
  print(f"o seu salaraio atual e de {salario_atual} teve um almento o seu salario foi para: {salariototal}")