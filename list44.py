def potencia_recursiva(base, exp):
    if exp ==0:
        return  1
    elif exp > 0:
        return base * potencia_recursiva(base, exp -1)
    else:
        return 1 / potencia_recursiva(base, -exp)
    