from model.Joueur import *

def main():
    abdel=Joueur(Nom='Abdel',Prenom='Abdelou')
    abdel.save()
    Joueur.getAllPlayers()
