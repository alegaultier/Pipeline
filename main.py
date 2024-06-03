from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    text = 'Oh... ¡"Hola, mundo"! Tratando de hacer la referencia al de Netflix en producción.'
    return text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 5000)