import mysql.connector
from mysql.connector import Error
from configparser import ConfigParser

class DataBase:
    @staticmethod
    def read_db_config(filename='src/db/conf.ini', section='MySQL'):
        parser = ConfigParser()
        parser.read(filename)
        
        db_config = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db_config[param[0]] = param[1]
        else:
            raise Exception(f'Section {section} not found in the {filename} file')
        
        return db_config

    @staticmethod
    def create_connection():
        db_config = DataBase.read_db_config()
        try:
            connection = mysql.connector.connect(**db_config) # Utilisation de ** pour envoyer les paramètres de connexion contenus dans db_confi
            return connection
        except Error as e:
            print("Error connecting to MySQL:", e)
            return None
    @staticmethod    
    def close_connection(connection):
        if connection:
            connection.close()
            print("MySQL connection closed.")


def main():
    connection = DataBase.create_connection()
    if connection :
        print ('cool')



if __name__ == "__main__":
    main()


def getAllQuestions():
    connexion = create_connection()
    cursor = connexion.cursor()

    try:
        query = "SELECT Texte FROM Question"
        cursor.execute(query)
        questions = cursor.fetchall()

        return [question[0] for question in questions]
    except Error as e:
        print("Error:", e)
    finally:
        if connexion.is_connected():
            connexion.close()

def getQuestionsWithTheme(theme_id):
    connexion = create_connection()
    cursor = connexion.cursor()

    try:
        query = f"SELECT Texte FROM Question WHERE ID_Theme = {theme_id}"
        cursor.execute(query)
        questions = cursor.fetchall()

        return [question[0] for question in questions]
    except Error as e:
        print("Error:", e)
    finally:
        if connexion.is_connected():
            connexion.close()

