from wtforms import Form
from wtforms import StringField, TextField
from wtforms.fields.html5 import EmailField
from wtforms import HiddenField

from wtforms import validators

def length_honeypot(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('El campo debe estar vacio')

class CommentForm(Form):
    username = StringField('username', [validators.length(min=4,max=25, message='Ingrese un nombre valido'), 
                                        validators.Required(message='El username es requerido')])
    email = EmailField('Correo Electronico',[
        validators.Required(message='El email es requerido'),
        validators.Email(message='Ingrese un email valido')
    ])
    comment = TextField('Comentario')
    honeypot = HiddenField('', [length_honeypot])