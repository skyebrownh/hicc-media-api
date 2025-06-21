import pytest

def test_get_all_users(test_client):
    response = test_client.get("/users")
    assert response.status_code == 200