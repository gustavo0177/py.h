from datetime import datetime

def formato_24h_para_12h(hora_24h):
    return datetime.strptime(hora_24h, "%H:%M").strftime("%I:%M %p")