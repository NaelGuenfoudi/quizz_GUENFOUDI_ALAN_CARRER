from tabulate import tabulate
import emoji
import mysql.connector

# Fonction pour afficher le menu de connexion ou d'inscription
def afficher_co_ins():
    print(tabulate([["----- Connexion/Inscription -----\n1. S'inscrire \n2. Se connecter\n3. Quitter"]], tablefmt='grid'))
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
        else:
            print("Choix invalide")
# Fonctions pour les différentes options du menu
def option1():
    print("S'inscrire")

def option2():
    print("Se connecter")

def option3():
    print("Au revoir")