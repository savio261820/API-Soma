from flask import Flask, request, jsonify
from functools import wraps
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# Em produção, isto viria de uma variável de ambiente
TOKEN_VALIDO = os.getenv("TOKEN_VALIDO")


# Decorator para proteger rotas com Bearer Token
def requer_token(funcao):
    @wraps(funcao)
    def envoltorio(*args, **kwargs):
        cabecalho = request.headers.get("Authorization", "")

        # Precisa começar com "Bearer "
        if not cabecalho.startswith("Bearer "):
            return jsonify({"erro": "Token ausente."}), 401

        # Extrai o token
        token = cabecalho.split(" ", 1)[1]

        # Verifica se o token é válido
        if token != TOKEN_VALIDO:
            return jsonify({"erro": "Token inválido."}), 401

        # Token válido
        return funcao(*args, **kwargs)

    return envoltorio


# =====================================================
# GET /api/soma (rota pública)
# =====================================================
@app.route("/api/soma", methods=["GET"])
def soma():
    return jsonify({
        "mensagem": "Esta é uma rota pública.",
        "dica": "Utilize POST /api/soma com Bearer Token para acessar a versão protegida da API."
    })


# =====================================================
# POST /api/soma (rota protegida)
# =====================================================
@app.route("/api/soma", methods=["POST"])
@requer_token
def soma_post():
    dados = request.get_json(silent=True) or {}

    a = dados.get("a")
    b = dados.get("b")

    cliente = request.headers.get("X-Cliente", "anonimo")

    if a is None or b is None:
        return jsonify({"erro": "Envie 'a' e 'b' no corpo JSON."}), 400

    return jsonify({
        "resultado": a + b,
        "chamado_por": cliente
    })


# =====================================================
# GET /api/protegido
# =====================================================
@app.route("/api/protegido", methods=["GET"])
@requer_token
def protegido():
    return jsonify({
        "mensagem": "Acesso autorizado! Dados secretos aqui."
    })


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)