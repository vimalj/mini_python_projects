import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

print(
    Fore.BLUE
    + Back.YELLOW
    + "Hi, My name is Python "
    + Fore.YELLOW
    + Back.BLUE
    + "I love open-source contribution"
)
print(Back.CYAN + "Hi, My name is Python")
print(Fore.RED + Back.GREEN + "Hi My name is Python")
