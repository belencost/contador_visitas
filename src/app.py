from flask import Flask, render_template, jsonify
from src.contador import ContadorClics

#Se dice a flask donde esta el codigo de la web
app = Flask(__name__, template_folder='../templates')

# Creamos nuestro contador usando la clase que armamos en el contador.py
contador = ContadorClics()

# Cuando alguien entra a la ruta principal ("/"), le mostramos la página web (index.html)
@app.route("/")
def index():
    return render_template("index.html")

# Cuando alguien hace clic en la página, se llama a esta ruta para sumar un clic
@app.route("/clics", methods=["POST"])
def registrar_visita():
    total = contador.incrementar()
    return jsonify({
        "mensaje": "Clic registrado con exito",
        "total_clics": total
    })

# Esta ruta nos permite consultar cuántos clics hay en cualquier momento
@app.route("/estado", methods=["GET"])
def obtener_estado():
    return jsonify({"total_actual": contador.obtener_clics()})

# Abrir servidor
if __name__ == "__main__":
    app.run()