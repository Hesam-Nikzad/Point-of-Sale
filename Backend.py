from typing import Type
import mysql.connector
import pandas as pd
import datetime
import jdatetime

def Insert_Auto_Increment(Table, List):

    query = 'SELECT * FROM %s;' %Table
    unit_of_measure_df = pd.read_sql(query, cnx)
    id = len(unit_of_measure_df) + 1
    List.insert(0, id)

    format_strings = ','.join(['%s'] * len(List))
    try: 
        cursor.execute('INSERT INTO %s VALUES (%s)' % (Table, format_strings), tuple(List))
        return 'Successfully added to the table %s' %Table
    except mysql.connector.Error as err:
        if err.errno == 1062: 
            return 'This is a redundant information'

    cnx.commit()

############# Main ##################

cnx = mysql.connector.connect(user='root', password='harchi', host='127.0.0.1', database='pos')
cursor = cnx.cursor()

Table = 'unit_of_measure'
List = ['مثقال']
print(Insert_Auto_Increment(Table, List))