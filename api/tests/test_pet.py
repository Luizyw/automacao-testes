import requests

BASE_URL = "https://petstore.swagger.io/v2"
PET_ID = 999999


def test_criar_pet():
    payload = {
        "id": PET_ID,
        "name": "doguinho_teste",
        "status": "available"
    }

    response = requests.post(f"{BASE_URL}/pet", json=payload)

    assert response.status_code == 200
    assert response.json()["name"] == "doguinho_teste"


def test_buscar_pet():
    response = requests.get(f"{BASE_URL}/pet/{PET_ID}")

    assert response.status_code == 200
    assert response.json()["id"] == PET_ID


def test_atualizar_pet():
    payload = {
        "id": PET_ID,
        "name": "doguinho_atualizado",
        "status": "sold"
    }

    response = requests.put(f"{BASE_URL}/pet", json=payload)

    assert response.status_code == 200
    assert response.json()["status"] == "sold"


def test_deletar_pet():
    response = requests.delete(f"{BASE_URL}/pet/{PET_ID}")

    assert response.status_code == 200