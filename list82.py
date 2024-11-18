from datetime import datetime

def dias_entre_datas(data1, data2):
    formato = "%d/%m/%Y"
    d1 = datetime.strptime(data1, formato)
    d2 = datetime.strptime(data2, formato)
    return abs((d2 - d1).days)