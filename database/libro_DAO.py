from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    def get_generi(self):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is not None:
            print("Connection estabilished")

            query = """SELECT DISTINCT genere 
                       FROM libro
                       WHERE genere IS NOT NULL"""
            cursor = cnx.cursor()
            cursor.execute(query)

            for row in cursor:
                if row[0]:
                    result.append(row[0])

            cursor.close()
            cnx.close()
        return result

    def get_libri_filtrati(self, biblioteca, genere):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is not None:
            print("Connection estabilished")

            query = """SELECT l.* 
                       FROM libro l, biblioteca b 
                       WHERE l.id_biblioteca = b.id 
                         AND b.nome = COALESCE(%s, b.nome) 
                         AND l.genere = COALESCE(%s, l.genere)"""
            cursor = cnx.cursor()
            cursor.execute(query, (biblioteca, genere))

            for row in cursor:
                libro = Libro(*row)
                result.append(libro)

            cursor.close()
            cnx.close()
        return result