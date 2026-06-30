import requests
import os
from dotenv import load_dotenv

load_dotenv()
URL = "http://127.0.0.1:5000/api/protegido"
TOKEN = os.getenv("TOKEN_VALIDO")	

# O token vai no cabecalho, no formato: Bearer <token>
cabecalhos = {"Authorization": f"Bearer {TOKEN}"}


print(">> Com token valido:")
r1 = requests.get(URL, headers=cabecalhos)
print(" ", r1.status_code, r1.json())
print(">> Sem token nenhum:")

r2 = requests.get(URL)
print(" ", r2.status_code, r2.json())
print(">> Com token errado:")

r3 = requests.get(URL, headers={"Authorization": "Bearer chute-errado"})
print(" ", r3.status_code, r3.json())

print("Status:", r1.status_code)
print("Headers:", r1.headers)
print("Conteúdo:")
print(r1.text)