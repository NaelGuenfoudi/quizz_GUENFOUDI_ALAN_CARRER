
import sys

from dal import *
import time
import os
import sys
from multiprocessing import Event, Manager, Process
from ctypes import c_char_p
import math


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
        isFinish=None
        self.score_max=0
        self.current_time_question=0
        self.global_time=0
        self.nbVie=3

    

   

    def next_question(self):
            if(self.is_alive()):
                self.current_question_number += 1
                self.pose_question_and_wait_for_answer()

   
    def is_alive(self):
        is_alive=True
        if(self.nbVie==0) :
            is_alive=False
            self.isFinish.set()
        return is_alive
        

    def afficherReponses(self, reponses):
        for i, reponse in enumerate(reponses):
            print(f"{i + 1}. {reponse[1]}")
    
    def isGoodReponse(id_current_response,id_current_question):
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

                

    def pose_question_and_wait_for_answer(self):
            if self.current_question_number <= len(self.questions):
                current_question = self.questions[self.current_question_number-1]
                self.display_question_and_options(current_question)
                time_for_question=get_time_question(current_question[0])
                user_answer = self.get_user_answer_with_timeout(time_for_question)
                
                if user_answer:
                    self.process_answer(user_answer, current_question)
                else:
                    print('\nTemps écoulé !')
                    
                return user_answer
            else:
                self.isFinish.set()

    def display_question_and_options(self, question):
        time_for_question=get_time_question(question[0])
        self.display_time_life(time_for_question)
        print(f"\nQuestion {self.current_question_number}: {question[1]}")
        
        
        responses = getReponsesForQuestion(question[0])
        self.afficherReponses(responses)

    def display_time_life(self,time_for_question):
        print(f'\n Tu as {time_for_question} secondes pour répondre')
        print(f'Il te reste {self.nbVie} vies')


    def get_user_answer_with_timeout(self,time_for_question):
        hasAnswer = Event()
        fn = sys.stdin.fileno()
        shared_value = Manager().Value(c_char_p, "")
        process_input = Process(target=Game.input_question, args=[fn, hasAnswer, shared_value])
        timeout = time_for_question
        start_time = time.time()  

        process_input.start()
        hasAnswer.wait(timeout)
        process_input.terminate()

        end_time = time.time()  

        elapsed_time = end_time - start_time  
        self.current_time_question = math.ceil(elapsed_time) if (elapsed_time - int(elapsed_time)) > 0.5 else int(elapsed_time)  # Arrondi
        return shared_value.value

    def process_answer(self, user_answer, current_question):
        response_index = int(user_answer) - 1
        id_response = getReponsesForQuestion(current_question[0])[response_index][0] # va chercher l'id de la réponse choisi
        if Game.isGoodReponse(id_response, current_question[0]):
            self.score += get_point_question(current_question[0])
        else :
            self.nbVie-=1    
        self.score_max+=get_point_question(current_question[0])
        self.global_time+=self.current_time_question



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
    def display_score(self):
        print (f'Tu as pris {self.current_time_question} secondes à répondre à la question et tu es à {self.score}/{self.score_max}')
        
    
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
            # Poser la prochaine question
            self.display_score()    
            self.next_question()   
              

        print(f'Merci d avoir joué , tu as eu un score de {self.score}/{self.score_max} en {self.global_time} secondes ')   
           
            


if __name__ == '__main__':
    game = Game()
    game.main()

