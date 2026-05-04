import requests

BASE_URL = "https://petstore.swagger.io/v2"
USERNAME = "luiz_teste_qa"


def test_criar_usuario():
    payload = {
        "id": 12345,
        "username": USERNAME,
        "firstName": "Luiz",
        "lastName": "Felipe",
        "email": "luiz@email.com",
        "password": "123456",
        "phone": "999999999",
        "userStatus": 1
    }

    response = requests.post(f"{BASE_URL}/user", json=payload)

    assert response.status_code == 200


def test_buscar_usuario():
    response = requests.get(f"{BASE_URL}/user/{USERNAME}")

    assert response.status_code == 200
    assert response.json()["username"] == USERNAME


def test_atualizar_usuario():
    payload = {
        "id": 12345,
        "username": USERNAME,
        "firstName": "Luiz Atualizado",
        "lastName": "Felipe",
        "email": "luiz.atualizado@email.com",
        "password": "123456",
        "phone": "888888888",
        "userStatus": 1
    }

    response = requests.put(f"{BASE_URL}/user/{USERNAME}", json=payload)

    assert response.status_code == 200


def test_deletar_usuario():
    response = requests.delete(f"{BASE_URL}/user/{USERNAME}")

    assert response.status_code == 200