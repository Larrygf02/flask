from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    name="Raul"
    return render_template('hola.html', name=name)

@app.route('/client/')
def client():
    list_name=["Raul","Juan","Kelly"]
    return render_template('client.html', list=list_name)

#con debug True, el servidor esta en la escucha de los cambios.
if __name__ == "__main__":
    app.run(debug=True, port=2500)