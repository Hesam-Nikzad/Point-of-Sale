from typing import Type
import mysql.connector
import pandas as pd
import datetime
import jdatetime

class SQL_Control:

    def __init__(self, user, password, host, database):
        self.cnx = cnx = mysql.connector.connect(user=user, password=password, host=host, database=database)
        self.cursor = cnx.cursor()
        print('Successfully connected to the MySQL database')

    def Insert_Auto_Increment(self, Table, List):

        query = 'SELECT * FROM %s;' %Table
        unit_of_measure_df = pd.read_sql(query, self.cnx)
        id = len(unit_of_measure_df) + 1
        List.insert(0, id)

        format_strings = ','.join(['%s'] * len(List))
        try: 
            self.cursor.execute('INSERT INTO %s VALUES (%s)' % (Table, format_strings), tuple(List))
            self.cnx.commit()
            return 'Successfully added to the table %s' %Table

        except mysql.connector.Error as err:
            if err.errno == 1062: 
                return 'This is a redundant information'

    def Edit_Row(self, Table, conidtion_column, condition, target_column, variable):
    
        try:
            self.cursor.execute('UPDATE %s SET %s = \'%s\' WHERE %s = \'%s\';' % (Table, target_column, variable, conidtion_column, condition))
            self.cnx.commit()
            return 'Successfully edited the row where %s = %s' %(conidtion_column, condition)

        except mysql.connector.Error as err:
            if err.errno == 1062: 
                return 'This is a redundant information'

    def Delete_Row(self, Table, conidtion_column, condition):
    
        self.cursor.execute('DELETE FROM %s WHERE %s = \'%s\';' % (Table, conidtion_column, condition))
        self.cnx.commit()
        return 'Successfully deleted the row where %s = %s' %(conidtion_column, condition)

    def Show_All_Rows_of_Table(self, Table):
        
        query = 'SELECT * FROM %s;' %Table
        df = pd.read_sql(query, self.cnx)
        df.sort_values(by=['id'], inplace=True)
        
        return df.to_dict('records')

############# Main ##################

#SQL = SQL_Control('root', 'harchi', '127.0.0.1', 'pos')

Table = 'unit_of_measure'
List = ['مثقال']
conidtion_column = 'id'
condition = '4'
target_column = 'name'
variable = 'بسته تک عددی'

#print(SQL.Insert_Auto_Increment(Table, List))
#print(SQL.Edit_Row(Table, conidtion_column, condition, target_column, variable))
#print(SQL.Delete_Row(Table, conidtion_column, condition))
#print(SQL.Show_All_Rows_of_Table(Table))