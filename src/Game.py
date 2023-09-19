
import sys

from dal import *
import time
import os
import sys
from multiprocessing import Event, Manager, Process
from ctypes import c_char_p


class Game:

    TOTAL_TIME= 60
    QUESTION_TIME= 10
    TOTAL_QUESTION= 5
    def __init__(self, ):
       
        self.theme = 1
        self.score = 0
        self.questions = []
        self.current_reponse = 0
        self.current_question_number = 0
        self.game_over = False
        self.question_over = False
        self.current_timer_question = None
        self.current_timer_global = None
        isFinish=None

    

   

    def next_question(self):
            self.current_question_number += 1
            self.ask_question()
        

    def afficherReponses(self, reponses):
        for i, reponse in enumerate(reponses):
            print(f"{i + 1}. {reponse[1]}")
    
    def isGoodReponse(text_response,id_current_question):
        id_current_response=get_id_reponse_for_text(text_response)
        id_good_reponse = getGoodResponseForQuestion(id_current_question)
        
        return id_good_reponse==id_current_response 

    def getGoodIdAnswerForCurrentQuestion(self, choice):
        return getReponsesForQuestion(self.current_question_number)[choice-1][0]

    def input_question(fn, hasAnwser, res):
        # Connexion entre la console principale et la console du process
        sys.stdin = os.fdopen(fn)

        # Récupération de la valeur
        userInput = input('Donne la réponse de la question: ')


        # On verifie que l'input n'est pas vide
        if (userInput == ''):
            print('Vous devez saisir une réponse correct !')

            # On relance la fonction de saisie
            Game.input_question(fn, hasAnwser, res)
        elif userInput not in ['1', '2', '3']:
            print('Veuillez saisir une réponse valide (1, 2 ou 3) !')
            # On relance la fonction de saisie
            Game.input_question(fn, hasAnwser, res)    
        else:
            # la valeure n'est pas vide on peut donc remplir la variable partageable

            res.value = userInput


            # Lancement de l'event pour signaler au timer qu'une valeure à été recupérée
            hasAnwser.set()

                

    def ask_question(self):
        if len(self.questions)> self.current_question_number or len(self.questions)== self.current_question_number:
            questionCurrent = self.questions[self.current_question_number-1]
            print(f"\nQuestion {self.current_question_number}: "+questionCurrent[1])
            # le but est de recuperer toutes les reponses de la question et de les afficher, mais je ne sais pas comment on gere ,aide moi gpt
            
            reponses = getReponsesForQuestion(questionCurrent[0])

            self.afficherReponses(reponses)

            hasAnwser = Event()

            fn = sys.stdin.fileno()

                # Création d'une variable partageable entre les process
            res = Manager().Value(c_char_p, "")

                # Création du process
            processInput = Process(target=Game.input_question, args=[fn, hasAnwser, res])

                # Définition du nombre de secondes à attendre
            timeout=Game.QUESTION_TIME

                # Lancement du process
            processInput.start()

                # Attente d'une réponse en fonction du temps défini sur timeout
            hasAnwser.wait(timeout)

                # Destruction du process
            processInput.terminate()

                # Si aucune valeur n'est entrée, cela signifie que le temps est écoulé
            print(f'Value de la réponse:{res.value}')    
            if (res.value == ''):
                print('\nTemps écoulé !') 
            else :
                reponse=int(res.value)-1
                text_reponse=reponses[reponse][1]
                if Game.isGoodReponse(text_reponse,questionCurrent[0]):
                    self.score+=1
                    
                    
            return res.value
        else:
            
            self.isFinish.set()


    def global_timer(isFinish):
        time.sleep(Game.TOTAL_TIME)  
        if not isFinish.is_set():
            print("\nLe timer global est écoulé !")
            isFinish.set()
        os._exit(0)     
            

    def get_theme_input():
        themes = getAllTheme()
        print('\nVoici les différents thèmes disponibles:')
        
        for theme in themes:
            print(f'{theme[0]}: {theme[1]}')
        
        idTheme = -1  # Initialisation à une valeur non valide
        while idTheme not in [theme[0] for theme in themes] and idTheme != 0:
            try:
                idTheme = int(input('\nChoisissez le thème avec lequel vous voulez jouer. Si vous voulez de tout, envoyez 0: '))
            except ValueError:
                print("Veuillez entrer un nombre valide.")
        
        return idTheme
    
    def set_questions_for_theme(self,id_theme):
        self.theme=id_theme
        self.questions=getQuestionsOfTheme(id_theme,Game.TOTAL_QUESTION)

    def main(self):
        id_theme=Game.get_theme_input()
        self.set_questions_for_theme(id_theme)
        isFinish = Event()
        self.isFinish=isFinish

        # Lancement du timer global
        processTimer = Process(target=Game.global_timer, args=[isFinish])
        processTimer.start()

        # Récupération du paramètre de connexion de la console principale
        fn = sys.stdin.fileno()

        # Tant que le timer global n'est pas terminé
        while not isFinish.is_set():
            # Poser la première question
            self.next_question()     

        score=5
        print(f'Merci d avoir joué , tu as eu {self.score} bonnes réponses, bravo')   
           
            


if __name__ == '__main__':
    game = Game()
    game.main()

