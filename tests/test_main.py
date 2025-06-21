def test_get_all_users(test_client, setup_user):
    response = test_client.get("/users")
    assert response.status_code == 200

    response_json = response.json()
    assert len(response_json) > 0
    assert response_json[0].get("user_id") == setup_user.get("user_id")

def test_get_single_user(test_client, setup_user):
    response = test_client.get(f"/users/{setup_user.get("user_id")}")
    assert response.status_code == 200

    response_json = response.json()
    assert len(response_json) == 1
    assert response_json[0].get("user_id") == setup_user.get("user_id")
    assert response_json[0].get("first_name") == "TEST"

def test_post_user(test_client, clean_users_table):
    invalid_json1 = {}
    invalid_json2 = {"first_name": "INVALID USER"}
    valid_json = {"first_name": "NEW", "last_name": "USER", "phone": "1235557890"}

    response1 = test_client.post("/users", json=invalid_json1)
    assert response1.status_code == 422 

    response2 = test_client.post("/users", json=invalid_json2)
    assert response2.status_code == 422 

    response = test_client.post("/users", json=valid_json)
    response_json = response.json()
    assert response.status_code == 200 
    assert response_json.get("first_name") == "NEW"
    assert response_json.get("is_active") == True 