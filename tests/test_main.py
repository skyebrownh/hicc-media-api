import pytest

def test_get_all_users(test_client, setup_user):
    response = test_client.get("/users")
    assert response.status_code == 200

    response_json = response.json()
    assert len(response_json) > 0
    assert response_json[0].get("user_id") == setup_user.get("user_id")