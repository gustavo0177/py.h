import pyfiglet
from colorama import Fore, Style

from colorama import init
init(autoreset=True)
text = "santos ta de volta"
ascii_art = pyfiglet.figlet_format(text,font="slant")

print(Fore.CYAN + Style.BRIGHT+ascii_art)
from colorama import Fore , Style ,init
init()
print(Fore.RED+"vermelho")
print(Fore.GREEN+"verde")
print(Fore.BLUE+"azul")
print(Fore.YELLOW+"amarelo")
print(Fore.WHITE+"branco")