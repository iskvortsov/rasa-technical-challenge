import pytest
import requests
from utils.random_generator import *

BASE_URL = "https://fakestoreapi.com"


def test_get_single_product():
    product_id = generate_int_in_range(1, 20)
    response = requests.get(f"{BASE_URL}/products/{product_id}")
    assert response.status_code == 200
    product = response.json()
    assert isinstance(product, dict)
    assert product['id'] == product_id


def test_get_limited_products():
    limit = generate_int_in_range(1, 20)
    response = requests.get(f"{BASE_URL}/products?limit={limit}")
    assert response.status_code == 200
    assert len(response.json()) == limit


def test_create_product():
    product_to_create = {
        "title": f"Test {generate_string()}",
        "price": generate_int_in_range(1, 200),
        "description": f"A test {generate_string()} description",
        "image": "https://i.pravatar.cc",
        "category": "test"
    }
    response = requests.post(f"{BASE_URL}/products", json=product_to_create)
    assert response.status_code == 200
    created_product = response.json()
    assert "id" in created_product, f"Created product doesn't have an ID"
    assert created_product["title"] == product_to_create["title"]
    assert created_product["price"] == product_to_create["price"]
    assert created_product["description"] == product_to_create["description"]
    assert created_product["image"] == product_to_create["image"]
    assert created_product["category"] == product_to_create["category"]


def test_update_product():
    product_id = generate_int_in_range(1, 20)
    update_json = {
        "title": f"Updated Product {generate_string()}",
        "price": generate_int_in_range(1, 200),
        "description": f"An updated product {generate_string()}",
        "image": "https://i.pravatar.cc",
        "category": generate_string()
    }

    response_put = requests.put(f"{BASE_URL}/products/{product_id}", json=update_json)
    assert response_put.status_code == 200
    updated_product = response_put.json()
    assert updated_product["id"] == product_id
    assert updated_product["title"] == update_json["title"]
    assert updated_product["price"] == update_json["price"]
    assert updated_product["description"] == update_json["description"]
    assert updated_product["image"] == update_json["image"]
    assert updated_product["category"] == update_json["category"]


def test_delete_product():
    product_id = generate_int_in_range(1, 20)
    response = requests.delete(f"{BASE_URL}/products/{product_id}")
    assert response.status_code == 200
    assert response.json()["id"] == product_id


@pytest.mark.parametrize("username, password, expected_status_code", [
    ("mor_2314", "83r5^_", 200),
    ("invalid_user", "invalid_password", 401)
])
def test_login_user(username, password, expected_status_code):
    auth_json = {
        "username": username,
        "password": password
    }

    response = requests.post(f"{BASE_URL}/auth/login", json=auth_json)
    assert response.status_code == expected_status_code
    if expected_status_code == 200:
        assert "token" in response.json()
