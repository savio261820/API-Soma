# API REST com Flask

Projeto desenvolvido para a disciplina de **Aplicação para Ambiente Web** do curso de **Bacharelado em Cibersegurança** da Universidade Federal de Uberlândia (UFU).

O objetivo deste projeto foi criar uma API REST utilizando **Flask**, aplicando conceitos de comunicação cliente-servidor, métodos HTTP e autenticação com Bearer Token.

---

## Funcionalidades

Durante o desenvolvimento foram implementadas as seguintes funcionalidades:

* ✅ API REST utilizando Flask;
* ✅ Requisição **GET** para realizar soma de dois números;
* ✅ Cliente Python consumindo a API com a biblioteca `requests`;
* ✅ Requisição **POST** enviando dados em JSON;
* ✅ Leitura de informações enviadas no cabeçalho (Header);
* ✅ Proteção de rota utilizando **Bearer Token**;
* ✅ Retorno de códigos HTTP apropriados (200, 400 e 401).

---

## Tecnologias utilizadas

* Python 3
* Flask
* Requests
* Git
* GitHub

---

## Estrutura do projeto

```text
.
├── servidor.py          # API Flask
├── cliente.py           # Consumo da rota GET
├── cliente_post.py      # Consumo da rota POST
├── cliente_token.py     # Teste da rota protegida
├── .gitignore
└── README.md
```

---

## Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git
cd SEU-REPOSITORIO
```

### 2. Crie um ambiente virtual

```bash
python -m venv venv
```

### 3. Ative o ambiente

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### 4. Instale as dependências

```bash
pip install flask requests
```

---

## Executando o servidor

```bash
python servidor.py
```

O servidor ficará disponível em:

```text
http://127.0.0.1:5000
```

---

## Endpoints

### GET `/api/soma`

Recebe dois números pela URL.

**Exemplo**

```http
GET /api/soma?a=2&b=3
```

**Resposta**

```json
{
  "resultado": 5
}
```

---

### POST `/api/soma`

Recebe os valores no corpo da requisição em formato JSON.

**Body**

```json
{
  "a": 10,
  "b": 7
}
```

Também utiliza o cabeçalho:

```http
X-Cliente: turma-ciberseguranca
```

**Resposta**

```json
{
  "resultado": 17,
  "chamado_por": "turma-ciberseguranca"
}
```

---

### GET `/api/protegido`

Rota protegida por Bearer Token.

**Header**

```http
Authorization: Bearer segredo-da-turma-123
```

**Resposta**

```json
{
  "mensagem": "Acesso autorizado! Dados secretos aqui."
}
```

Caso o token esteja incorreto ou ausente, a API retorna:

```http
401 Unauthorized
```

---

## Clientes disponíveis

O projeto possui três scripts para testar a API:

| Arquivo            | Função                                |
| ------------------ | ------------------------------------- |
| `cliente.py`       | Consome a rota GET                    |
| `cliente_post.py`  | Consome a rota POST                   |
| `cliente_token.py` | Testa a autenticação com Bearer Token |

---

## Conceitos praticados

Durante este projeto foram trabalhados conceitos importantes como:

* APIs REST;
* Comunicação cliente-servidor;
* Métodos HTTP (GET e POST);
* JSON;
* Cabeçalhos HTTP;
* Códigos de status HTTP;
* Autenticação com Bearer Token;
* Versionamento com Git e GitHub.

---

## Licença

Este projeto foi desenvolvido apenas para fins acadêmicos.
