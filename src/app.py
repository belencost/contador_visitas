from flask import Flask, render_template, jsonify
from src.contador import ContadorVisitas

#Se dice a flask donde esta el codigo de la web
app = Flask(__name__, template_folder='../templates')

# Creamos nuestro contador usando la clase que armamos en el contador.py
contador = ContadorVisitas()

# Cuando alguien entra a la ruta principal ("/"), le mostramos la página web (index.html)
@app.route("/")
def index():
    return render_template("index.html")

# Cuando alguien hace clic en la página, se llama a esta ruta para sumar una visita
@app.route("/visita", methods=["POST"])
def registrar_visita():
    total = contador.incrementar()
    return jsonify({
        "mensaje": "Hola, visitaste este sitio",
        "total_visitas": total
    })

# Esta ruta nos permite consultar cuántas visitas hay en cualquier momento
@app.route("/estado", methods=["GET"])
def obtener_estado():
    return jsonify({"total_actual": contador.obtener_visitas()})

# Abrir servidor
if __name__ == "__main__":
    app.run()