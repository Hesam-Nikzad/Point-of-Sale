from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return 'Hello World!'

if __name__ == '__main__':
    print('The Python Flask server is running')
    app.run(port=50000)