from ..db.database import *

class BaseModel:
    TABLE_NAME = None

    def save(self):
        conn = DataBase.create_connection()
        cursor = conn.cursor()

        if hasattr(self, 'ID'):
            # Mettre à jour l'enregistrement existant
            columns = [col for col in self.__dict__.keys() if col != 'ID']
            values = [self.__dict__[col] for col in columns]
            set_clause = ', '.join(f"{col} = ?" for col in columns)
            cursor.execute(f"UPDATE {self.TABLE_NAME} SET {set_clause} WHERE ID = ?", values + [self.ID])
        else:
            # Créer un nouvel enregistrement
            columns = self.__dict__.keys()
            values = list(self.__dict__.values())
            cursor.execute(f"INSERT INTO {self.TABLE_NAME} ({', '.join(columns)}) VALUES ({', '.join(['%s'] * len(values))})", values)
        
        conn.commit()
        
    @staticmethod
    def execute_query(query, params=None):
        # Assuming DataBas_connection() is a function that gives a database connection.
        conn = DataBase.create_connection()
        cursor = conn.cursor()

        try:
            # If no params are passed, we'll default to an empty tuple
            params = params or ()

            cursor.execute(query, params)
            conn.commit()
            
            # We might want to decide if we need to fetch data based on query type
            if query.strip().lower().startswith("select"):
                return cursor.fetchall()
            else:
                return cursor

        except Exception as e:
            print(f"Error executing query: {e}")
            # In the case of an error, you might want to return None or raise the error, depending on your requirements.
            return None

        finally:
            if conn.is_connected():
                conn.close()
