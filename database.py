import mysql.connector


def conectar():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="252514",
        database="escola"
    )
    return conexao