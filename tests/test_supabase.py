import pytest
from app.utils.supabase import *

def test_supabase_post(supabase_service, clean_teams_table):
    response = supabase_service.post("teams", body={"team_name": "TEST TEAM", "lookup": "testteam"})
    assert response.get("team_name") == "TEST TEAM"
    assert response.get("lookup") == "testteam"

    with pytest.raises(TypeError):
        supabase_service.post()

    with pytest.raises(TypeError):
        supabase_service.post(None)

    with pytest.raises(HTTPException, match="API Error"):
        supabase_service.post("invalid_table", {"team_name": "VALID", "lookup": "valid"})
    
    with pytest.raises(HTTPException, match="API Error"):
        supabase_service.post("teams", {})

    with pytest.raises(HTTPException, match="API Error"):
        supabase_service.post("teams", [])

    with pytest.raises(HTTPException, match="Not Found"):
        supabase_service.post("teams", "invalid")

    with pytest.raises(HTTPException, match="API Error"):
        supabase_service.post("teams", {"team_name": "TEST"})

    with pytest.raises(HTTPException, match="API Error"):
        supabase_service.post("teams", {"lookup": "test"})

def test_supabase_get_all(supabase_service, clean_teams_table):
    # setup: insert teams
    supabase_service.post("teams", body={"team_name": "Team 1", "lookup": "team1"})
    supabase_service.post("teams", body={"team_name": "Team 2", "lookup": "team2"})

    response = supabase_service.get("teams")
    assert len(response) > 0
    assert response[0].get("team_name") == "Team 1"
    assert response[1].get("lookup") == "team2"

    with pytest.raises(TypeError):
        supabase_service.get()

    with pytest.raises(HTTPException, match="API Error"):
        supabase_service.get(None)

    with pytest.raises(HTTPException, match="API Error"):
        supabase_service.get("invalid_table")

def test_supabase_get(supabase_service, clean_teams_table):
    # setup: insert teams
    team_a = supabase_service.post("teams", body={"team_name": "Team A", "lookup": "team_a"})
    team_b = supabase_service.post("teams", body={"team_name": "Team B", "lookup": "team_b"})

    responseA = supabase_service.get("teams", id=team_a.get("team_id"))
    responseB = supabase_service.get("teams", id=team_b.get("team_id"))

    assert responseA[0].get("team_name") == "Team A"
    assert responseB[0].get("lookup") == "team_b"
    assert responseB[0].get("team_id") == team_b.get("team_id")

def test_supabase_update(supabase_service, clean_teams_table):
    # setup: insert team
    update_team = supabase_service.post("teams", body={"team_name": "UPDATE ME", "lookup": "updateteam"})

    supabase_service.update("teams", body={"team_name": "NEW"}, id=update_team.get("team_id"))
    response = supabase_service.get("teams", id=update_team.get("team_id"))

    assert response[0].get("team_name") == "NEW"
    assert response[0].get("lookup") == "updateteam"

def test_supabase_delete(supabase_service, clean_teams_table):
    # setup: insert team
    delete_team = supabase_service.post("teams", body={"team_name": "DELETE ME", "lookup": "deleteme"})

    delete_response = supabase_service.delete("teams", id=delete_team.get("team_id"))

    assert delete_response.get("team_id") == delete_team.get("team_id")
    assert delete_response.get("lookup") == "deleteme" 

    with pytest.raises(HTTPException, match="Not Found"):
        supabase_service.get("teams", id=delete_team.get("team_id"))

# helper functions
def test_table_id():
    assert table_id("users") == "user_id"
    assert table_id("user_availability") == "user_availability_id"

def test_validate(supabase_service, clean_teams_table):
    # setup: insert team
    supabase_service.post("teams", body={"team_name": "TEST", "lookup": "test"})

    query_api_error = supabase_service.client.table("invalid").select("*")
    with pytest.raises(HTTPException, match="API Error"):
        validate(query_api_error)

    query_not_found_error = supabase_service.client.table("teams").select("*").eq("team_id", "00000000-0000-0000-0000-000000000000")
    with pytest.raises(HTTPException, match="Not Found"):
        validate(query_not_found_error)
    
    query = supabase_service.client.table("teams").select("*")
    response = validate(query)
    assert len(response.data) > 0