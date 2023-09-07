from tabulate import tabulate
import emoji


# Fonction pour afficher le menu
def afficher_theme():
    print(tabulate([["----- Choix du theme -----\n1. Sport\n2. Automobile\n3. Culture Generale\n4. Jeux Vidéos"]], tablefmt='grid'))
    while True:
        reponse = input("Veuillez entrer votre choix: ")
        if len(reponse) < 1:
            print("La valeur de la réponse ne peux pas être nulle")
        elif reponse == "1":
            option1()
            break
        elif reponse == "2":
            option2()
            break
        elif reponse == "3":
            option3()
            break
        elif reponse == "4":
            option4()
            break
        else:
            print("Choix invalide")
    # Fonctions pour les différentes options du menu
def option1():
    print("\U0001F3C0""Vous avez choisi le sport""\U0001F3C6")

def option2():
    print("\U0001F697""Vous avez choisi lautomobile""\U0001F697")

def option3():
    print("\U0001F30F""Vous avez choisi la culture générale""\U0001F30F")
    
def option4():
    print("\U0001F3AE""Vous avez choisi les jeux vidéos""\U0001F3AE")
