from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from functools import lru_cache
import os

app = Flask(__name__)

# Cache for name-to-image mapping to improve performance
@lru_cache(maxsize=128)
def get_image_for_name(nombre):
    """Cached function to get image filename for a given name"""
    name_to_image = {
        "arturo": "arturo.jpeg",
        "julian": "julian.jpeg", 
        "gina": "gina.jpeg"
    }
    return name_to_image.get(nombre.lower())

@app.route("/", methods=["GET", "POST"])
def index():
    nombre = None
    imagen = None

    if request.method == "POST":
        # Botón para borrar
        if "borrar" in request.form:
            return redirect(url_for("index"))

        # Procesar el formulario con optimización
        nombre_input = request.form.get("nombre", "").strip()
        if nombre_input:
            imagen = get_image_for_name(nombre_input)
            if imagen:
                nombre = nombre_input.lower()

    return render_template("index.html", nombre=nombre, imagen=imagen)

# Optimize static file serving
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)
