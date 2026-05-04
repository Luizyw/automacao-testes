# Automação de Testes - API e Web

## Descrição
Este projeto tem como objetivo automatizar testes de API e Web utilizando boas práticas de desenvolvimento, garantindo qualidade, organização e integração contínua.

---

## Tecnologias Utilizadas

- Python
- Pytest
- Requests
- Selenium
- WebDriver Manager
- GitHub Actions (CI/CD)

---

## API Testada

Base URL:
https://petstore.swagger.io/v2

### Endpoints cobertos:

- User (CRUD completo)
- Pet (CRUD completo)
- Store (operações principais)

---

## Automação Web

Sistema testado:
https://www.saucedemo.com/

### Fluxo automatizado (E2E):

- Login
- Adicionar produto ao carrinho
- Acessar carrinho
- Realizar checkout
- Validar mensagem de sucesso

---

## Boas Práticas

- Utilização do padrão Page Object Model
- Código organizado por responsabilidades
- Separação entre testes e páginas
- Uso de asserts para validação

---

## Integração Contínua (CI/CD)

Pipeline configurada com GitHub Actions para execução automática dos testes a cada push no repositório.

- Testes de API executados automaticamente
- Integração contínua garantida

---

## Estrutura do Projeto

automacao-testes/
│
├── api/
│   └── tests/
│
├── web/
│   ├── pages/
│   └── tests/
│
├── .github/
│   └── workflows/
│
├── requirements.txt
└── README.md

---

## Como Executar o Projeto

### 1. Criar ambiente virtual

python -m venv venv

---

### 2. Ativar ambiente

Windows:
venv\Scripts\Activate.ps1

---

### 3. Instalar dependências

pip install -r requirements.txt

---

### 4. Executar testes de API

python -m pytest api/tests

---

### 5. Executar testes Web

python -m pytest web/tests

---

## Autor

Luiz Felipe