import os
from colors import light_blue, light_red, red, white

def clear_terminal():
    if os.name == "nt":
        os.system('cls')  # Pour Windows
    else:
        os.system('clear')  # Pour les autres systèmes d'exploitation

def perdu():
    print("\r\U0001F480\033[31m You lose !\033[0m \U0001F480")

