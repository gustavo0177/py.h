def produto(a, b):
    if b == 0:
        return 0
    elif b > 0:
        return a +produto(a, b- 1)
    else:
        return -produto(a, -b)