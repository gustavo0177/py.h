while True:

 populacao_a =  int(input("digite o numero da primeira populacao: "))
 populacao_b =  int(input("digite o numero da segunda  populacao: "))
 taxa_a = int(input(" digite a primira taixa da populacao: "))
 taxa_b = int(input(" digite a seguanda taixa da populacao: "))
 ano = 0
 while populacao_a < populacao_b:
    populacao_a += populacao_a * taxa_a / 100
    populacao_b += populacao_b * taxa_b / 100
    ano += 1
    
 print(f" e necessario {ano} anos para a populacao A passar B")
 break