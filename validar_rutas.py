from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return 'hola mundo'

@app.route('/saluda/')
@app.route('/saluda/<name>/<int:num>/')
def saluda(name='Un valor por default', num=0):
    return 'Estoy saludando {} {}'.format(name, num)

if __name__ == "__main__":
    app.run(debug=True, port=2500)