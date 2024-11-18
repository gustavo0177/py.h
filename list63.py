def calcula_juros(cap, tax, temmp):
    montante = cap * (1+ tax) ** temmp
    return montante