from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    title = 'Curso de flask'
    return render_template('index2.html', title=title)

#con debug True, el servidor esta en la escucha de los cambios.
if __name__ == "__main__":
    app.run(debug=True, port=2500)