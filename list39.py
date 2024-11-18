def aproxima_pi(n):
    pi_aproximado = 0
    sinal =1

    for i in range(n):
        termo =sinal * (4/ (2*i+1))
        pi_aproximado += termo
        sinal *= -1

    return pi_aproximado