from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    text = 'Oh... es un "Hola, mundo" similar al que tiene Netflix en su página principal. ¡Qué original!'
    return text

if __name__ == '__main__':
    app.run(host='0.0.0.0')