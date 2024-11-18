from datetime import datetime, timedelta

def adiciona_dias(data, n):
    formato = "%d/%m/%Y"
    data_obj = datetime.strptime(data, formato)
    nova_data = data_obj + timedelta(days=n)
    return nova_data.strftime(formato)