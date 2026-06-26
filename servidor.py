from flask import Flask, request, jsonify

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

if __name__ == "__main__":
	app.run(host="127.0.0.1", port=5000, debug=True)