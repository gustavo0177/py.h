from datetime import datetime

def formato_12h_para_24h(hora_12h):
    return datetime.strptime(hora_12h, "%I:%M %p").strftime("%H:%M")