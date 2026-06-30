from flask import Flask, request, jsonify
from functools import wraps
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
# Rota 1: GET http://127.0.0.1:5000/api/soma?a=2&b=3
@app.route("/api/soma", methods=["GET"])
def soma():
	# Le os parametros ’a’ e ’b’ da URL (query string)
	a = request.args.get("a", type=float)
	b = request.args.get("b", type=float)

	# Validacao simples (passo na direcao de "aplicacoes seguras")
	if a is None or b is None:
		return jsonify({"erro": "informe a e b, ex: ?a=2&b=3"}), 400

	return jsonify({"resultado": a + b})

# Rota 2: POST http://127.0.0.1:5000/api/soma (dados no CORPO em JSON)
@app.route("/api/soma", methods=["POST"])
def soma_post():
	dados = request.get_json(silent=True) or {}
	a = dados.get("a")
	b = dados.get("b")

	# Le um parametro enviado no CABECALHO (header) da requisicao
	cliente = request.headers.get("X-Cliente", "anonimo")

	if a is None or b is None:
		return jsonify({"erro": "envie a e b no corpo JSON"}), 400

	return jsonify({"resultado": a + b, "chamado_por": cliente})

# Em producao, isto viria de variavel de ambiente, NUNCA no codigo!
# :)
TOKEN_VALIDO = os.getenv("TOKEN_VALIDO")


def requer_token(funcao):
    @wraps(funcao)
    def envoltorio(*args, **kwargs):
        cabecalho = request.headers.get("Authorization", "")

        # 1) precisa começar com "Bearer "
        if not cabecalho.startswith("Bearer "):
            return jsonify({"erro": "token ausente"}), 401

        # 2) extrai o token
        token = cabecalho.split(" ", 1)[1]

        # 3) verifica o token
        if token != TOKEN_VALIDO:
            return jsonify({"erro": "token invalido"}), 401

        # Token válido
        return funcao(*args, **kwargs)

    return envoltorio

@app.route("/api/protegido", methods=["GET"])
@requer_token
def protegido():
	return jsonify({"mensagem": "Acesso autorizado! Dados secretos aqui."})


if __name__ == "__main__":
	app.run(host="127.0.0.1", port=5000, debug=True)