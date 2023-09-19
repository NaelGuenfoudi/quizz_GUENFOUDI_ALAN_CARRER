#!/usr/bin/python3

import os
from dal import *
import random
import maskpass
import time
import string
import mysql.connector
import bcrypt   
from quizz import *


players = {}

def generate_random_password(length=24):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def center_text(text, width):
    padding = (width - len(text)) // 2
    centered_text = ' ' * padding + text
    return centered_text

def clear_screen():
    if os.name == 'nt':
        os.system('cls')  # Windows
    else:
        os.system('clear')  # Posix

def login(username):
    try:
        password_from_db=get_password_from_username(username)
    except Error as e:
        print(f"Une erreur est survenue: {e}")

    while True:
        password = maskpass.askpass(prompt="Veuillez entrer votre mot de passe: ", mask="")
        if len(password) < 1:
            print("\x1b[31mLa valeur du mot de passe ne peut pas être nulle.\x1b[0m")
        elif len(password) >= 255:
            print("\x1b[31mLe mot de passe ne peut pas dépasser 255 caractères.\x1b[0m")
        else:
            if bcrypt.checkpw(password.encode('utf-8'), password_from_db.encode('utf-8')):
                print("\x1b[32mAuthentification réussie !\x1b[0m")
                time.sleep(2)
                start_game()
            else:
                print("\x1b[31mMot de passe incorrect.\x1b[0m")
                time.sleep(3)
                main()

def admin(username):
    try:
        
            password_from_db = get_password_from_username(username)
    except Error as e:
        print(f"Une erreur est survenue: {e}")

    while True:
        password = maskpass.askpass(prompt="Veuillez entrer votre mot de passe: ", mask="")
        if len(password) < 1:
            print("\x1b[31mLa valeur du mot de passe ne peut pas être nulle.\x1b[0m")
        elif len(password) >= 255:
            print("\x1b[31mLe mot de passe ne peut pas dépasser 255 caractères.\x1b[0m")
        else:
            if bcrypt.checkpw(password.encode('utf-8'), password_from_db.encode('utf-8')):
                if is_admin(username):
                    print("\x1b[31mL'utilisateur n'est pas administrateur.\x1b[0m")
                    time.sleep(2)
                    main()
                else:
                    print("\x1b[32mAuthentification réussi et rôle administrateur détécter.\x1b[0m")
                    time.sleep(2)
                    menu_administrateur_goodpass()
            else:
                print("\x1b[31mMot de passe incorrect.\x1b[0m")
                time.sleep(3)
                main()

def quizzGame():
    clear_screen()
    while True:
        username = input("Veuillez entrer votre nom d'utilisateur: ")

        if len(username) < 4:
            print("\x1b[31mLa valeur ne peut pas être inférieure à 4\x1b[0m")
        elif len(username) > 60:
            print("\x1b[31mLa valeur ne peut pas être plus grande que 60\x1b[0m")
        else:
            try:
                
                if is_user(username):
                    print('if_is_user')
                    login(username)
                else:
                    print("Création du compte.")
                    while True:
                        password = maskpass.askpass(prompt="Veuillez entrer votre mot de passe: ", mask="")

                        if len(password) < 1:
                            print("\x1b[31mLa valeur du mot de passe ne peut pas être nulle.\x1b[0m")
                        elif str(password) == str(username):
                            print("\x1b[31mLa valeur du mot de passe ne peut pas être la même que le nom d'utilisateur.\x1b[0m")
                        elif len(password) >= 255:
                            print("\x1b[31mLe mot de passe ne peut pas dépasser 255 caractères.\x1b[0m")
                        else:
                            break

                    while True:
                        password_validation = maskpass.askpass(prompt="Veuillez valider votre mot de passe: ", mask="")

                        if len(password_validation) < 1:
                            print("\x1b[31mLa valeur du mot de passe ne peut pas être nulle.\x1b[0m")
                        elif str(password_validation) != str(password):
                            print("\x1b[31mLes mots de passe ne correspondent pas.\x1b[0m")
                        elif len(password_validation) >= 255:
                            print("\x1b[31mLe mot de passe ne peut pas dépasser 255 caractères.\x1b[0m")
                        else:
                            break

                    insert_user(username,password_validation,0)
                    break
            except Exception as e:
                print(f"Une erreur s'est produite : {e}")
                
def start_game():
    clear_screen()
    print("\x1b[31m──────────────────")
    clear_screen()
    time.sleep(0.5)
    print("\x1b[31m──────────────────")
    print("\x1b[31m──\x1b[0m▄▄\x1b[31m─────\x1b[0m▄\x1b[31m───\x1b[0m▄▄▄▄▄")
    clear_screen()
    time.sleep(0.5)
    print("\x1b[31m──────────────────")
    print("\x1b[31m──\x1b[0m▄▄\x1b[31m─────\x1b[0m▄\x1b[31m───\x1b[0m▄▄▄▄▄")
    print("\x1b[0m▄▀\x1b[31m──\x1b[0m▀▄\x1b[31m──\x1b[0m█\x1b[31m─\x1b[0m█\x1b[31m──\x1b[0m█\x1b[31m───\x1b[0m█")
    clear_screen()
    time.sleep(0.5)
    print("\x1b[31m──────────────────")
    print("\x1b[31m──\x1b[0m▄▄\x1b[31m─────\x1b[0m▄\x1b[31m───\x1b[0m▄▄▄▄▄")
    print("\x1b[0m▄▀\x1b[31m──\x1b[0m▀▄\x1b[31m──\x1b[0m█\x1b[31m─\x1b[0m█\x1b[31m──\x1b[0m█\x1b[31m───\x1b[0m█")
    print("\x1b[0m█\x1b[31m────\x1b[0m█\x1b[31m─\x1b[0m█\x1b[31m───\x1b[0m█\x1b[31m─\x1b[0m█\x1b[31m───\x1b[0m█")
    clear_screen()
    time.sleep(0.5)
    print("\x1b[31m──────────────────")
    print("\x1b[31m──\x1b[0m▄▄\x1b[31m─────\x1b[0m▄\x1b[31m───\x1b[0m▄▄▄▄▄")
    print("\x1b[0m▄▀\x1b[31m──\x1b[0m▀▄\x1b[31m──\x1b[0m█\x1b[31m─\x1b[0m█\x1b[31m──\x1b[0m█\x1b[31m───\x1b[0m█")
    print("\x1b[0m█\x1b[31m────\x1b[0m█\x1b[31m─\x1b[0m█\x1b[31m───\x1b[0m█\x1b[31m─\x1b[0m█\x1b[31m───\x1b[0m█")
    print("\x1b[31m─\x1b[0m▀▄▄▀\x1b[31m─\x1b[0m▐▄▄▄▄▄▌█▄▄▄█")
    clear_screen()
    time.sleep(0.5)
    print("\x1b[31m──────────────────")
    print("\x1b[31m──\x1b[0m▄▄\x1b[31m─────\x1b[0m▄\x1b[31m───\x1b[0m▄▄▄▄▄")
    print("\x1b[0m▄▀\x1b[31m──\x1b[0m▀▄\x1b[31m──\x1b[0m█\x1b[31m─\x1b[0m█\x1b[31m──\x1b[0m█\x1b[31m───\x1b[0m█")
    print("\x1b[0m█\x1b[31m────\x1b[0m█\x1b[31m─\x1b[0m█\x1b[31m───\x1b[0m█\x1b[31m─\x1b[0m█\x1b[31m───\x1b[0m█")
    print("\x1b[31m─\x1b[0m▀▄▄▀\x1b[31m─\x1b[0m▐▄▄▄▄▄▌█▄▄▄█")
    print("\x1b[31m──────────────────")

    while True:
        choix = input("\x1b[31mÊtes-vous sûr de vouloir jouer ? \x1b[0m")
        if choix.lower() == "oui":
            clear_screen()
            break
        elif choix.lower() == "non":
            main()
            break
        else:
            print("\x1b[31mOui ou non ?")

    os_width = os.get_terminal_size().columns


    print(center_text("\x1b[31mBienvenue dans SquizGame\x1b[0m", os_width))
    print(center_text("Les règles sont simples : vous avez 5 vies et 10 questions générées aléatoirement.", os_width))
    print(center_text("Chaque vie peut être perdue de 2 manières différentes :", os_width))
    print(center_text(" • En ne répondant pas dans le temps imparti.", os_width))
    print(center_text(" • En donnant la mauvaise réponse.", os_width))
    print(center_text("Le niveau des questions peut varier.", os_width))
    print(center_text("Nous espérons que votre culture est bonne, car elle sera mise à rude épreuve.", os_width))
    print()
    print(center_text("Vous avez un délais de 5 seconde avant l'affichage de la première question", os_width))
    print(center_text("Vous pouvez quitter le quizz quand vous le souhaiter, mais votre action ne sera pas sans conséquence", os_width))
    print()
    

def multiplayer_start():
    global reponse
    reponse = {}

    for i in range(1, len(players)+1):
        reponse[players[i]] = input(f"{players[i]}: ")
        
def multiplayer():
    clear_screen()
    while True:
        choix = input("Combien de joueur êtes-vous ? ")

        try:
            choix_int = int(choix)
        except ValueError:
            print("\x1b[31mErreur de saisie\x1b[0m")
            continue

        if len(choix) < 1:
            print("\x1b[31mLa valeur ne peux pas être nul\x1b[0m")

        if choix_int > 5:
            print("\x1b[36mNous pouvons supporter qu'à 5 joueurs maximum\x1b[0m")
        
        if 1 <= choix_int <= 5:
            break
        else:
            print("\x1b[31mLe nombre de joueurs doit être compris entre 1 et 5\x1b[0m")

    for i in range(1, choix_int + 1):
        username = input(f"Joueur {i}: ")
        players[i] = username

    multiplayer_start()

def highScore():
    print(("High score"))

def menu_administrateur_goodpass():
    clear_screen()
    print(("1. Ajouter une question"))
    print(("2. Supprimer une question"))
    print(("3. Changer un mot de passe"))
    print(("4. Supprimer un utilisateur"))
    print(("5. Changer les permissions utilisateur"))
    print(("6. Retourner au menu principal"))
    print(("0. Quitter le programme"))
    print()
    while True:
        choix = input("> ")
        if choix == "0":
            exit(0)
        elif choix == "1":
            clear_screen()
            while True:
                question = input("Veuillez entrer l'intitulé de votre question: ")
                if len(question) < 1:
                    print("\x1b[31mLa question ne peut pas être nulle\x1b[0m")
                else:
                    while True:
                        reponse = input("Veuillez entrer la réponse valide à la question: ")
                        if len(reponse) < 1:
                            print("\x1b[31mLa réponse ne peut pas être nulle\x1b[0m")
                        else:
                            while True:
                                fausse_reponse = input("Veuillez entrer les fausses réponses (séparer par un \";\"): ")
                                if len(fausse_reponse) < 1:
                                    print("\x1b[31mLa valeur ne peut pas être nulle\x1b[0m")
                                elif ";" not in fausse_reponse:
                                    print("\x1b[31mNous n'avons pas détecter le caractères séparateur\x1b[0m")
                                elif fausse_reponse.count(";") != 2:
                                    print("\x1b[31mNous n'avons pas détecter le bon nombre de caractère séparateur.\x1b[0m")
                                elif ";" in fausse_reponse:
                                    splitted = fausse_reponse.split(";")
                                    if len(splitted) != 3:
                                        print("\x1b[31mLe nombre de réponse n'est pas valide.\x1b[0m")
                                    elif any(val.strip() == "" for val in splitted):
                                        print("\x1b[31mUne ou plusieurs valeurs sont vides\x1b[0m")
                                    else:
                                        # Traitement SQL pour ajouter la nouvelle question. insert_question_with_responses(question,good_answer,bad_answers)
                                        print("\x1b[32mQuestion ajouter avec succès\x1b[0m")
                                        time.sleep(2)
                                        menu_administrateur_goodpass()                                      
        elif choix == "2":
            # Traitement pour afficher les questions
            break
        elif choix == "3":
            while True:
                clear_screen()
                afficher_all_users()
                print()
                print("Pour quitter le programme, écriver `\x1b[32mexit\x1b[0m`")
                print()
                username = input("Veuillez entrer le nom de l'utilisateur: ")
                if len(username) < 1:
                    print("\x1b[31mLa valeur ne peut pas être nulle.\x1b[0m")
                elif len(username) > 60:
                    print("\x1b[31mLa valeur ne peut pas être supérieure à 60 caractères\x1b[0m")
                elif username.lower() == "exit":
                    menu_administrateur_goodpass()
                else:
                    # Vérifiez d'abord si l'utilisateur existe dans la base de données
                    existing_user = is_user(username)

                    if existing_user:
                        random_password = generate_random_password()
                        salt = bcrypt.gensalt()
                        hashed_password = bcrypt.hashpw(random_password.encode('utf-8'), salt)
                        try:
                            update_password(username,hashed_password)
                            print("\x1b[32mLe mot de passe a été changé avec succès.\x1b[0m")
                            print(f"\x1b[1;33mVoici le nouveau mot de passe pour {username}: \x1b[0m{random_password}")
                            input("Appuyer sur [ENTREE] pour continuer")
                            menu_administrateur_goodpass()
                        except mysql.connector.Error as e:
                            print(f"\x1b[31mUne erreur est survenue: {e}\x1b[0m")
                    else:
                        print(f"\x1b[31mL'utilisateur {username} n'existe pas dans la base de données.\x1b[0m")
                        time.sleep(2)
            continue  # Revenez au début de la boucle if
        elif choix == "4":
            while True:
                clear_screen()
                afficher_all_users()
                print()
                print("Pour quitter le programme, écriver `\x1b[32mexit\x1b[0m`")
                print()
                user = input("Veuillez entrer l'utilisateur que vous souhaitez supprimer: ")
                if len(user) < 1:
                    print("\x1b[31mLa valeur ne peut pas être nulle.\x1b[0m")
                elif len(user) > 60:
                    print("La valeur ne peut pas être supérieure à 60 caractères")
                elif user.lower() == "exit":
                    menu_administrateur_goodpass()
                else:
                    # Vérifiez d'abord si l'utilisateur existe dans la base de données
                    
                    existing_user = is_user(username)

                    if existing_user:
                        while True:
                            sure = input("Êtes-vous sûr de votre choix ? ")
                            if len(sure) < 1:
                                print("\x1b[31mLa valeur ne peut pas être nulle.\x1b[0m")
                            elif len(sure) > 3:
                                print("Veuillez répondre par \"oui\" ou \"non\"")
                            elif sure.lower() == "oui":
                                try:
                                    delete_user(username)
                                    print(f"L'utilisateur {user} a été supprimé avec succès.")
                                except mysql.connector.Error as e:
                                    print(f"Une erreur s'est produite lors de la suppression de l'utilisateur : {e}")
                                menu_administrateur_goodpass()
                            elif sure.lower() == "non":
                                print("\x1b[33mL'utilisateur ne sera pas supprimé.\x1b[0m")
                                time.sleep(2)
                                menu_administrateur_goodpass()
                            else:
                                print("\x1b[31mChoix invalide\x1b[0m")
                        break  # Sortez de la boucle externe
                    else:
                        print(f"\x1b[31mL'utilisateur {user} n'existe pas dans la base de données.\x1b[0m")
                        time.sleep(2)
            continue  # Revenez au début de la boucle if
        elif choix == "5":
            while True:
                clear_screen()
                afficher_all_users()
                print()
                print("Pour quitter le programme, écriver `\x1b[32mexit\x1b[0m`")
                print()
                username = input("Veuillez entrer le nom d'utilisateur: ")
                if len(username) < 1:
                    print("\x1b[31mLa valeur ne peut pas être nulle.\x1b[0m")
                elif len(username) > 60:
                    print("\x1b[31mLa valeur ne peut pas être supérieure à 60 caractères\x1b[0m")
                elif username.lower() == "exit":
                    menu_administrateur_goodpass()
                else:
                    # Vérifiez d'abord si l'utilisateur existe dans la base de données
                    existing_user = is_user(username)

            if existing_user:
                clear_screen()
                print(f"Utilisateur: {username}\n")
                print("1. Ajouter les permissions administrateur")
                print("2. Supprimer les permissions administrateur")
                print()

                while True:
                    perm = input("> ")

                    if perm not in ["1", "2"]:
                        print("\x1b[31mErreur de saisie. Veuillez choisir 1 ou 2.\x1b[0m")
                        continue

                    try:
                        if perm == "1":
                            set_admin(username)
                            print(f"\x1b[32mLes permissions administratives de l'utilisateur {username} ont été accordées avec succès.\x1b[0m")
                        else:
                            remove_admin(username)
                            print(f"\x1b[32mLes permissions administratives de l'utilisateur {username} ont été retirées avec succès.\x1b[0m")

                        time.sleep(2)
                        menu_administrateur_goodpass()

                    except mysql.connector.Error as e:
                        print(f"Une erreur s'est produite lors de la mise à jour des permissions administratives : {e}")
                        menu_administrateur_goodpass()

                    break  # Sortez de la boucle interne

            else:
                print(f"\x1b[31mL'utilisateur {username} n'existe pas dans la base de données.\x1b[0m")
                time.sleep(2)

                continue  # Revenez au début de la boucle if
        elif choix == "6":
                    main()
                    break  
        else:
                    print(("\x1b[31mErreur de saisie\x1b[0m"))
            
def afficher_all_users():
                usernames=get_all_usernames()
                print("Liste des utilisateurs:\n")
                i=1
                for username in usernames:
                        print(f"- {i}. {username[0]}")
                        i+=1   
def menu_administrateur():
    clear_screen()
    while True:
        username = input("Veuillez entrer votre nom d'utilisateur: ")

        if len(username) < 4:
            print("\x1b[31mLa valeur ne peut pas être inférieure à 4\x1b[0m")
        elif len(username) > 60:
            print("\x1b[31mLa valeur ne peut pas être plus grande que 60\x1b[0m")
        else:
            try:
                result=is_user(username)
                if result:
                    admin(username)
                else:
                    print("\x1b[31mLe compte n'existe pas\x1b[0m")
            except mysql.connector.Error as e:
                print(f"Une erreur s'est produite: {e}")

def main():
    clear_screen()
    print(("1. Lancer le quiz"))
    print(("2. Lancer le mode multijoueur"))
    print(("3. Affichage du menu high-score"))
    print(("4. Menu administrateur"))
    print(("0. Quitter le quiz"))
    print()
    while True:
        choix = input("> ")
        if choix == "0":
            print(("Merci d'avoir jouer ! Au plaisir de vous revoir ;)"))
            exit(0)
        elif choix == "1": # Quizz
            quizzGame()
            break
        elif choix == "2": # Mutijoueur
            multiplayer()
            break
        elif choix == "3": # High-score
            highScore()
            break
        elif choix == "4": # Administrateur
            menu_administrateur()
            break
        else:
            print(("\x1b[31mErreur de saisie\x1b[0m"))

if __name__ == "__main__":
    main()