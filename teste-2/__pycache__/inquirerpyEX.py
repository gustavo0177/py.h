
from  InquirerPy  import inquirer

def valida_email(val):
    if "@" not in val:
        raise ValueError ("por favor , insira um email valido")
    return val
email = inquirer.text("qual e o seu email?", validate=valida_email).execute