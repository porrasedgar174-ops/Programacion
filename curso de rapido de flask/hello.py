from wtforms.validators import DataRequired, Length

# Importa campos de formulario
from wtforms import StringField, PasswordField, SubmitField
from flask_wtf import FlaskForm  # Importa FlaskForm para formulari
from datetime import datetime  # Importa la clase datetime
from markupsafe import escape  # Importa la función escape
# Importa Flask y render_template para plantillas HTML. conectar html con flask y python.
from flask import Flask, render_template, url_for, request

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='dev'
)

# Filtros perzonalizados


@app.add_template_filter
def today(date):
    """Convierte la fecha en un formato más amigable"""
    return date.strftime('%d-%m-%Y')

# app.add_template_filter(today, 'today') dos formas de decorar la fecha ''


# funcion perzonalizada
# decorador
@app.add_template_global
def repeat(s, n):
    return s * n

# app.add_template_global(repeat, 'repeat') otra forma de decorar la funcion repea


@app.route('/')
# @app.route('/index')
def index():
    print(url_for('index'))
    print(url_for('hello'))
    print(url_for('code', code='print("Hola")'))
    name = "Alexander!"
    friends = ['Maria', 'Pedro', 'Juan', 'Karla']
    date = datetime.now()
    return render_template(
        'index.html',
        name=name,
        friends=friends,
        date=date

    )

# string variable
# int variable
# float variable
# path variable
# uuid variable


@app.route('/hello')
@app.route('/hello/<name>')
@app.route('/hello/<name>/<int:age>')
@app.route('/hello/<name>/<int:age>/<email>')
def hello(name=None, age=None, email=None):
    my_data = {
        'name': name,
        'age': age,
        'email': email
    }
    return render_template('hello.html', data=my_data)

    # if name == None and age == None:
    #     return '<h1>Hola, Mundo!</h1>'
    # elif age == None:
    #     return f'<h1>Hola, {name}!</h1>'
    # else:
    #     return f'<h1>Hola, {name} y tu edad es {age * 2}!</h1>'


@app.route('/code/<path:code>')
def code(code):
    return f'<code>{escape(code)}</code>'


# Crear formulario wtform


class RegisterForm(FlaskForm):
    username = StringField("Nombre de usuario:", validators=[
                           DataRequired(), Length(min=4, max=25)])
    password = PasswordField("Contraseña: ", validators=[
                             DataRequired(), Length(min=6, max=40)])
    submit = SubmitField("Registrar: ")


# Registrar usuario

@app.route('/auth/register', methods=['Get', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        return f"Nombre de usuario: {username}, Contraseña: {password}"

    # if request.method == 'POST':
    #     username = request.form['username']
    #     password = request.form['password']

    #     if len(username) >= 4 and len(username) <= 25 and len(password) >= 6 and len(password) <= 40:
    #         return f"Nombre de usuario: {username}, Contraseña: {password}"
    #     else:
    #         error = """ Nombre de usuario debe tener entre 4 y 25 caracteres.
    #             Contraseña debe tener entre 6 y 40 caracteres."""

    #         return render_template('auth/register.html', form=form,  error=error)

    return render_template('auth/register.html', form=form)
