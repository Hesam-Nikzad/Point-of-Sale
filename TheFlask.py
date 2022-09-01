from flask import Flask, jsonify, request
from Backend import SQL_Control

SQL = SQL_Control('root', 'harchi', '127.0.0.1', 'pos')

app = Flask(__name__)

@app.route('/welcome', methods=['GET'])
def welcome():
    
    List_of_Units= SQL.Show_All_Rows_of_Table('unit_of_measure')
    resp = jsonify(List_of_Units)
    resp.headers.add('Access-Control-Allow-Origin', '*')
    
    return resp

if __name__ == '__main__':
    print('The Python Flask server is running')
    app.run(port=50000)