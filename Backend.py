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
        cnx.commit()
        return 'Successfully added to the table %s' %Table

    except mysql.connector.Error as err:
        if err.errno == 1062: 
            return 'This is a redundant information'

def Edit_Row(Table, conidtion_column, condition, target_column, variable):
 
    try:
        cursor.execute('UPDATE %s SET %s = \'%s\' WHERE %s = \'%s\';' % (Table, target_column, variable, conidtion_column, condition))
        cnx.commit()
        return 'Successfully edited the row where %s = %s' %(conidtion_column, condition)

    except mysql.connector.Error as err:
        if err.errno == 1062: 
            return 'This is a redundant information'

############# Main ##################

cnx = mysql.connector.connect(user='root', password='harchi', host='127.0.0.1', database='pos')
cursor = cnx.cursor()

Table = 'unit_of_measure'
List = ['مثقال']
conidtion_column = 'id'
condition = '4'
target_column = 'name'
variable = 'بسته تک عددی'
#print(Insert_Auto_Increment(Table, List))
#print(Edit_Row(Table, conidtion_column, condition, target_column, variable))