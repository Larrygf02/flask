from flask import Flask
from flask import render_template
#se usa template_folder si queremos utilizar otra carpeta para guardar las
#plantillas, por defecto es la carpeta templates
#app = Flask(__name__, template_folder = "prueba")
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#con debug True, el servidor esta en la escucha de los cambios.
if __name__ == "__main__":
    app.run(debug=True, port=2500)