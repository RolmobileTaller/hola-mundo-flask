from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hola Mundo desde Flask!'

@app.route('/info')
def info():
    return 'Esta es una aplicación Flask básica lista para Railway'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
