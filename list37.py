def eh_armstronh(n):
    digits= [int(digits)for digits in str(n)]
    potencia = len (digits)
    soma = sum(digits ** potencia for digits in digits)
    return soma == n


print(eh_armstronh(153))