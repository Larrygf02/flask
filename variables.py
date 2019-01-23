from flask import Flask
from flask import render_template
#se usa template_folder si queremos utilizar otra carpeta para guardar las
#plantillas, por defecto es la carpeta templates
#app = Flask(__name__, template_folder = "prueba")
app = Flask(__name__)

@app.route('/user/<name>/')
def saluda(name='Raul'):
    age = 25
    my_list = [1,2,3,4]
    return render_template('user.html', name=name, age=age, list=my_list)

#con debug True, el servidor esta en la escucha de los cambios.
if __name__ == "__main__":
    app.run(debug=True, port=2500)