from wtforms import Form
from wtforms import StringField, TextField
from wtforms.fields.html5 import EmailField

from wtforms import validators

class CommentForm(Form):
    username = StringField('username', [validators.length(min=4,max=25, message='Ingrese un nombre valido'), 
                                        validators.Required(message='El username es requerido')])
    email = EmailField('Correo Electronico',[
        validators.Required(message='El email es requerido'),
        validators.Email(message='Ingrese un email valido')
    ])
    comment = TextField('Comentario')