from flask import Flask, jsonify
import random


class server:
    """
    Clase que crea un servidor Flask.
    """

    def __init__(self):
        """
        Cosntructor de la clase server.
        """

        self.server = Flask(__name__)

        self.register_routes()

    def register_routes(self):
        """
        Método que registra las rutas del servidor.
        """

        @self.server.route('/')
        def index():
            return "<h1>Hola Bienvenido a la etapa 1!</h1>"

        @self.server.route('/Hola')
        @self.server.route('/Hola/<nombre>')
        def hola_nombre(nombre=None):
            if nombre == None:
                return '<h1>Hola bienvenido, ¿Cual es tu nombre?!</h1>'
            else:
                return f'<h1>Hola, {nombre} binevenido, ¿Cual es tu edad?!</h1>'

        @self.server.route('/Hola/<nombre>/<int:edad>')
        def hola_edad(nombre=None, edad=None):
            if nombre == None and edad == None:
                return '<h1>Hola bienvenido, ¿Cual es tu nombre?!</h1>'
            elif edad == None:
                return f'<h1>Hola {nombre} binevenido, ¿Cual es tu edad?!</h1>'
            else:
                return f'<h1>Hola {nombre} binevenido, tu edad es {edad}, ¿Cual es tu email?!.</h1>'

        @self.server.route('/Hola/<nombre>/<int:edad>/<email>')
        def hola_email(nombre=None, edad=None, email=None):
            if nombre == None and edad == None and email == None:
                return '<h1>Hola bienvenido, ¿Cual es tu nombre?!</h1>'
            elif edad == None and email == None:
                return f'<h1>Hola {nombre} binevenido, ¿Cual es tu edad?|</h1>'
            elif email == None:
                return f'<h1>Hola {nombre} binevenido, tu edad es {edad}, ¿Cual es tu email?!</h1>'
            else:
                return f'<h1>Hola {nombre} binevenido, tu edad es {edad} y tu email es {email}.</h1>'

        @self.server.route('/Usuario')
        def usuario():
            datos = [
                {'nombre': 'Yepes', 'edad': random.randint(15, 56)},
                {'nombre': 'Andres', 'edad': random.randint(15, 56)},
                {'nombre': 'Camilo', 'edad': random.randint(15, 56)},
                {'nombre': 'Santiago', 'edad': random.randint(15, 56)},
                {'nombre': 'Juan', 'edad': random.randint(15, 56)}
            ]

            return jsonify(datos)

    def run(self):
        """
        Método que inicia el servidor.
        """
        self.server.run(debug=True)


if __name__ == '__main__':
    server_web = server()
    server_web.run()
