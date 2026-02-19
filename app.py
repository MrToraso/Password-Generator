from flask import Flask, render_template, request, jsonify
import string
import secrets
import os

print("RUNNING FROM:", os.getcwd())

app = Flask(__name__)

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

    # límite seguro
    if longitud > 40:
        longitud = 40

    if longitud < 6:
        longitud = 6


    password = generar_password(longitud)

    return jsonify({"password": password})

if __name__ == "__main__":

    app.run()
