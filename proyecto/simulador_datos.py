# Carga el modulo estandar para leer y escribir archivos CSV
import csv
# Carga el mosulo para generar numeros aleatorios
import random


class simuladordatos:
    """
    Clase para simular datos y guardarlos en un archivo CSV
    """

    # Metodo constructor
    def __init__(self, n_muestras: int = 100):
        self.n_muestras = n_muestras
        self.datos = []

    def generar_datos(self):
        """
        Genera datos simulados (Temperatura, Presion, tiempo)'
        """
        if self.datos:  # Si ya hay datos, no genera de nuevo
            print("Datos ya generados, usando los existentes.")
            return self.datos

        for i in range(self.n_muestras):
            registro = {
                'id': i + 1,
                'temperatura': round(random.uniform(15.0, 60.0), 2),
                'presion': round(random.uniform(1000, 1020), 2),
                'tiempo': i + 1
            }
            self.datos.append(registro)
            # Añade el registro a la lista self.datos

        return self.datos
        # Devuelve la lista completa para inspección o uso posterior

    def guardar_csv(self, nombre_archivo: str = "datos_simulados.csv"):
        """
        Guarda los datos simulados en un archivo CSV
        """
        # Evita guardar si no se generaron datos; lanza una excepción clara
        if not self.datos:
            raise ValueError("No hay datos generados para guardar.")

        # Abre el archivo para escritura y crea si no existe; newline="" evita líneas en blanco extras
        with open(nombre_archivo, "w", newline="") as archivo:
            campos = ["id", "temperatura", "presion", "tiempo"]

            # Configura un escritor que toma diccionarios y mapea claves a columnas
            writer = csv.DictWriter(archivo, fieldnames=campos)

            # Escribe la primera fila con los nombres de columnas
            writer.writeheader()

            # Escribe cada diccionario de self.datos como una fila
            writer.writerows(self.datos)

        # Devuelve la ruta/nombre del archivo para confirmación o uso posterior
        return nombre_archivo
