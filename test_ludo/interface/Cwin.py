import os
from colors import light_blue, light_red, red, white

def clear_terminal():
    if os.name == "nt":
        os.system('cls')  # Pour Windows
    else:
        os.system('clear')  # Pour les autres systèmes d'exploitation


def win():
    print("\r\033[32m\U0001F389 You win !\033[32m\U0001F389")
