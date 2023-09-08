from timer import *
import sys
import threading
from dal import *


class Game:
    def __init__(self, total_questions=10, time_per_question=15, total_time=60):
        self.total_questions = total_questions
        self.time_per_question = time_per_question
        self.total_time = total_time
        self.current_reponse = 0
        self.current_question_number = 0
        self.game_over = False
        self.question_over = False
        self.current_timer_question = None
        self.current_timer_global = None

    def start_timer_question(self, duration, callback):
        """Lance un timer qui s'exécute en arrière-plan."""
        self.current_timer_question = None
        self.current_timer_question = threading.Timer(duration, callback)
        self.current_timer_question.start()

    def start_timer_global(self, duration, callback):
        """Lance un timer qui s'exécute en arrière-plan."""
        self.current_timer_question = None
        self.current_timer_global = threading.Timer(duration, callback)
        self.current_timer_global.start()

    def close_timer_question(self):
        """Annule le timer actuel s'il est en cours d'exécution."""

        self.current_timer_question.cancel()

    def time_for_question_is_up(self):

        self.question_over = True

    def time_global_is_up(self):
        print("\nTemps global écoulé!")
        self.game_over = True

    def next_question(self):
        print('next_question')
        if not self.game_over and self.current_question_number < self.total_questions:
            self.current_question_number += 1
            self.ask_question()
        else:
            print("Fin du jeu!")

    def afficherReponses(self, reponses):
        for i, reponse in enumerate(reponses):
            print(f"{i + 1}. {reponse[1]}")

    def ask_question(self):
        print('ask_question')
        questionCurrent = getTextQuestionId(self.current_question_number)
        print(f"\nQuestion {self.current_question_number}: "+questionCurrent)
        # le but est de recuperer toutes les reponses de la question et de les afficher, mais je ne sais pas comment on gere ,aide moi gpt
        reponses = getReponsesForQuestion(self.current_question_number)

        self.afficherReponses(reponses)
        # Ici, nous lançons un timer pour cette question
        self.start_timer_question(10, self.time_for_question_is_up)

    def get_user_input(self):
        answerValid=True
        while not answerValid:
            reponse_choisi = input("Votre réponse (1, 2 ou 3): ")
            if self.user_input.isdigit() and 1 <= int(self.user_input) <= 3:
                self.current_reponse=reponse_choisi
                break

    def isGoodReponse(self):
        id_good_reponse = getGoodResponseForQuestion(
            self.current_question_number)
        return id_good_reponse == self.current_reponse

    def getGoodIdAnswerForCurrentQuestion(self, choice):
        return getReponsesForQuestion(self.current_question_number)[choice-1][0]

    def main(self):
        # Lancer le timer global pour l'ensemble du jeu.
        self.start_timer_global(self.total_time, self.time_global_is_up)

        # Boucle d'attente de réponse de l'utilisateur
        while not self.game_over:
            answerIsValid = False
            # Poser la première question
            self.next_question()        
            thread_input=threading.Thread(target=self.get_user_input)
            thread_input.start()
            
           
            self.close_timer_question()
            if self.isGoodReponse():
                print("ça gagne")
            print(self.question_over)
            self.question_over = False


game = Game()
game.main()
