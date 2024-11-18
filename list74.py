def ordena_por_valores(dic):
    return dict(sorted(dic.items(), key=lambda item: item[1]))