import mysql.connector


def SQL_Connect():
    cnx = mysql.connector.connect(user='root', password='harchi',
                              host='127.0.0.1',
                              database='pos')

    cursor = cnx.cursor()

    return cursor


