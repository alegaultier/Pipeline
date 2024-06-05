from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    text = 'Oh... ¡Hola, mundo! Esto es una referencia al que tenia Netflix en producción. Me quiero morir, las ganas de llorar son increibles, y más sabiendo que esto sigue fallando...'
    return text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 5000)