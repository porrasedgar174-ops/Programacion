# 🧠 Proyecto Flask --- Generación y Descarga de Datos Experimentales

Este proyecto combina las **Etapas 1, 2 y 3 del aprendizaje Flask**:\

- **Generar datos simulados** (temperatura, presión, tiempo).\
- **Visualizarlos en una tabla HTML.**\
- **Descargarlos como archivo CSV.**

---

## 📦 Estructura del proyecto

    proyecto/
    │
    ├── app.py
    ├── simulador_datos.py
    ├── datos_simulados.csv
    │
    ├── templates/
    │   ├── base.html
    │   └── datos.html
    │   └── generar_datos.html
    │   └── index.html
    │
    │
    └── static/
        ├── css/
        │    └── style.css
        ├── js/
        │    └── main.js
        └── img

---

## ⚙️ Requisitos

- Python 3.8 o superior
- Flask

Instálalo con:

```bash
pip install flask
```

---

## 🚀 Ejecución del proyecto

1️⃣ Clona o descarga la carpeta del proyecto.\
2️⃣ Abre la terminal en la carpeta del proyecto.\
3️⃣ Ejecuta el servidor Flask:

```bash
python app.py
```

4️⃣ Abre tu navegador y entra en:

    http://127.0.0.1:5000/

---

## 🧩 Rutas principales

Ruta Descripción

---

`/` Página de inicio
`/generar-datos` Genera y muestra los datos simulados (solo una vez)
`/datos` Descarga el archivo CSV con los datos
`/descargar` Descargar el archivo

---

## 💾 Comportamiento del simulador

- Si **no existe** `datos_simulados.csv`, se genera automáticamente.\
- Si **ya existe**, se cargan los datos desde ese archivo (no se
  regeneran).\
- Para **regenerar nuevos datos**, borra manualmente
  `datos_simulados.csv` y vuelve a ejecutar la app.

---

## 🧠 Tecnologías usadas

- **Flask** --- framework web en Python.
- **Jinja2** --- motor de plantillas HTML.
- **CSV** --- almacenamiento simple de datos.
- **HTML + CSS** --- interfaz web básica.

---

## ✨ EDGAR ALEXANDER PORRAS ROJAS

Desarrollado como parte del **Proyecto de Programación 2025** --- Flask
y manejo de datos experimentales.
