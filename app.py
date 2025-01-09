from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    nombre = None
    imagen = None

    if request.method == "POST":
        # Botón para borrar
        if "borrar" in request.form:
            return redirect(url_for("index"))  # Redirige a la ruta principal para reiniciar

        # Procesar el formulario para mostrar la imagen de carga e imagen principal
        nombre = request.form.get("nombre").lower()
        if nombre in ["arturo", "julian", "gina"]:
            if nombre == "arturo":
                imagen = "arturo.jpeg"
            elif nombre == "julian":
                imagen = "julian.jpeg"
            elif nombre == "gina":
                imagen = "gina.jpeg"
        else:
            nombre = None  # Nombre inválido

    return render_template("index.html", nombre=nombre, imagen=imagen)

if __name__ == "__main__":
    app.run(debug=True)
