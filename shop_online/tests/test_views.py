import pytest


@pytest.mark.django_db
def test_user(client):
    response = client.get('/shop/user/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_product(client):
    response = client.get('/shop/product/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_category(client):
    response = client.get('/shop/category/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_basket(client):
    response = client.get('/shop/cart/')
    assert response.status_code == 401
