from flask import Flask, render_template, url_for, jsonify, send_file
# send_file me sirve para enviar archivos al usuario
# jsonify me sirve para devolver datos en formato json
# render_template me srive para renderizar las plantillas html, conectar el backend con el frontend
# url_for me sirve para crear rutas dinamicas
from simulador_datos import simuladordatos


simulador = simuladordatos()


class app:
    """
    Clase principal que encapsula la palicacion Flask y sus rutas
    """

    def __init__(self):
        # Se crea la instancias de flask
        self.app = Flask(__name__)
        # Se registran las rutas
        self.register_routes()

    def register_routes(self):
        """
         Registra todas las rutas (endpoints) de la aplicación
        """
        # definimpos o crea,os las rutas
        @self.app.route('/')
        def index():
            print(url_for('index'))
            print(url_for('generar_datos'))
            return render_template(
                'index.html'
            )

        @self.app.route('/generar-datos')
        def generar_datos():
            print(url_for('generar_datos'))
            return render_template(
                'generar_datos.html',


            )

        @self.app.route('/datos')
        def datos():
            datos = simulador.generar_datos()
            simulador.guardar_csv("datos_simulados.csv")
            return render_template(
                "datos.html",
                datos=datos
            )

        @self.app.route('/descargar')
        def descargar():
            return send_file("datos_simulados.csv", as_attachment=True)
            # as_attachment=True fuerza la descarga del archivo. (“Guardar archivo como…”)
            # Si no se pone, el navegador intentará abrir el archivo directamente

    def ejecutar(self):
        """
        Ejecuta la aplicación Flask
        """
        # Activamos el depurador
        self.app.run(debug=True)


# Punto de entrada del programa; solo se ejecuta si es el archivo principal, si no esta no pasa nada
if __name__ == '__main__':
    app_web = app()  # Se crea el objeto de la clase
    app_web.ejecutar()  # Se ejecuta la aplicación


# app = Flask(__name__)


# @app.route('/')
# def index():
#     print(url_for('index'))
#     print(url_for('generar_datos'))
#     return render_template(
#         'index.html'
#     )

#     # return 'Hola Mundo desde Flask!'


# @app.route('/generar-datos')
# def generar_datos():
#     print(url_for('generar_datos'))
#     return render_template(
#         'generar_datos.html'
#     )


# @app.route('/descargar')
# def descargar():
#     return render_template(
#         'descargar.html'
#     )


# # Permite que el servidor se ejecute sin errores
# if __name__ == '__main__':
#     app.run(debug=True)
