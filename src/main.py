from dal import *

def choisirNiveau():
    levels=getAllLevel()
    print (levels)
    print('voici tous les niveau:')
    for id, (num, nom) in enumerate(levels):
        print(str(id) + ': ' + nom)

    niveauChoisi=None
    goodNumero=False

    while not goodNumero:
        niveauChoisi=input('Veuillez choisir le niveau voulu en y donnant son numero')
        if niveauChoisi.isdigit() and 0 <= int(niveauChoisi) < len(levels):
            goodNumero = True
        else:
            print("Numéro invalide.")
    
    return levels[int(niveauChoisi)-1]

def main():
   niveauChoisi=choisirNiveau()
   idThemeChoisi=1
   questions=getQuestionsOfThemeAndLevel(idThemeChoisi,niveauChoisi)
   

main()

