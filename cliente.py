import requests
import os
from dotenv import load_dotenv

load_dotenv()

URL = "http://127.0.0.1:5000/api/soma"
TOKEN = os.getenv("TOKEN_VALIDO")

print("Você deseja utilizar números fixos [1] ou inserir valores [2]?")
escolha = input("Insira: ")

if escolha == "1":
    corpo = {
        "a": 10,
        "b": 7
    }

elif escolha == "2":
    corpo = {
        "a": float(input("Insira o valor de A: ")),
        "b": float(input("Insira o valor de B: "))
    }

else:
    print("Opção inválida.")
    exit()

cabecalhos = {
    "Authorization": f"Bearer {TOKEN}",
    "X-Cliente": "turma-ciberseguranca"
}

resposta = requests.post(
    URL,
    json=corpo,
    headers=cabecalhos
)

print("Status:", resposta.status_code)
print("Corpo:", resposta.json())