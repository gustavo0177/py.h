def fibonacci_gen(n):

 if __name__ == "__main__":

    termos = int(input("Quantos termos da sequência de Fibonacci você deseja gerar? "))
    print("Sequência de Fibonacci:")
    for numero in fibonacci_gen(termos):
        print(numero, end=" ")