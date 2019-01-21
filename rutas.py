from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return 'hola mundo'

@app.route('/saluda')
def saluda():
    param = request.args.get('nombre','raul')
    return 'Estoy saludando {}'.format(param)

if __name__ == "__main__":
    app.run(debug=True, port=2500)