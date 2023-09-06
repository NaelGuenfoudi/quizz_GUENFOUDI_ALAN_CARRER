from .BaseModel import *
from ..db.database import *


class Joueur(BaseModel):
    TABLE_NAME = 'joueur'

    def __init__(self, Nom=None, Prenom=None):
        self.Nom = Nom
        self.Prenom = Prenom

    def parler(self,parole=None):
        print(f"{self.Prenom}+parole")

    @staticmethod
    def getAllPlayers():
        query = f"SELECT * FROM {Joueur.TABLE_NAME}"
        conn = DataBase.get_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        return cursor.fetchall()
        return BaseModel.execute_query(query,[])
    
    def from_db(cls, player_id):
    
        
        query=f"SELECT ID, Nom, Prenom FROM {cls.TABLE_NAME} WHERE ID = %s", (player_id,)
        cursor=BaseModel.execute_query(query,[])
        row = cursor.fetchone()
        
        if row:
            # Destructure les données et crée une instance de Joueur
            ID, Nom, Prenom = row
            return cls(ID=ID, Nom=Nom, Prenom=Prenom)
        else:
            # Retourne None si aucun joueur avec cet ID n'est trouvé
            return None

    
def main():
   qt1=Joueur('Quentin','Onsenfout')
   qt1.parler()
   qt1.save()
   playersData=Joueur.getAllPlayers()
   for playerData in playersData :
       playerCurrent=Joueur.from_db(Joueur,playerData[1])
       playerCurrent.parler

if __name__ == '__main__':
    main()
