from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'hola mundo'

#con debug True, el servidor esta en la escucha de los cambios.
if __name__ == "__main__":
    app.run(debug=True, port=2500)