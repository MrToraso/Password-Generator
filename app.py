from flask import Flask, render_template, request, jsonify
import string
import secrets

app = Flask(__name__, template_folder="../templates", static_folder="../static")

def generar_password(longitud=16):
    caracteres = string.ascii_letters + string.digits + "!@#$%"
    return "".join(secrets.choice(caracteres) for _ in range(longitud))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    longitud = int(data.get("longitud", 16))

    if longitud > 40:
        longitud = 40
    if longitud < 6:
        longitud = 6

    password = generar_password(longitud)
    return jsonify({"password": password})

app = app

