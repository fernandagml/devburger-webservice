import mysql.connector as sql

def conectar():
    conec = sql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="root",
        database="db_devburguer"
    )

    #Criando o cursor
    cursor = conec.cursor(dictionary=True)
    return conec, cursor