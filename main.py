from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    text = 'Proyectillo miedo terror de Redes de Computadores. Hecho por Alexander Gutiérrez, Anthony Li  y Sebastián Alvaréz. Un poquillo mañoso este proyecto.'
    return text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 5000)