from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import string

app = Flask(__name__)
CORS(app)

@app.route("/gerar_senha", methods=["POST"])
def gerar_senha():
    data = request.json

    usar_maiusculas = data.get("maiusculas", True)
    usar_numeros = data.get("numeros", True)
    usar_simbolos = data.get("simbolos", True)

    caracteres = string.ascii_lowercase

    if usar_maiusculas:
        caracteres += string.ascii_uppercase
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation
    if not caracteres:
        return jsonify({"erro": "Nenhum tipo de caractere selecionado. "}), 400
    
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))

    return jsonify({"senha": senha})

if __name__ == "__main__":
    app.run(debug=True)


