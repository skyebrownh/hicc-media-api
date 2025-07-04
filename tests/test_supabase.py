import pytest
from fastapi import HTTPException

from app.utils.supabase import validate

def test_supabase_post(supabase_service, clean_teams_table):
    response = supabase_service.post("teams", body={"team_name": "TEST TEAM", "lookup": "testteam"})
    assert response.get("team_name") == "TEST TEAM"
    assert response.get("lookup") == "testteam"

    with pytest.raises(TypeError):
        supabase_service.post()

    with pytest.raises(TypeError):
        supabase_service.post(None)

    with pytest.raises(HTTPException, match="does not exist"):
        supabase_service.post("invalid_table", {"team_name": "VALID", "lookup": "valid"})
    
    with pytest.raises(HTTPException, match="null violation"):
        supabase_service.post("teams", {})

    with pytest.raises(HTTPException, match="parse"):
        supabase_service.post("teams", [])

    with pytest.raises(HTTPException, match="not found"):
        supabase_service.post("teams", "invalid")

    with pytest.raises(HTTPException, match="null violation"):
        supabase_service.post("teams", {"team_name": "TEST"})

    with pytest.raises(HTTPException, match="null violation"):
        supabase_service.post("teams", {"lookup": "test"})

def test_supabase_get_all(supabase_service, clean_teams_table):
    # setup: insert teams
    supabase_service.post("teams", body={"team_name": "Team 1", "lookup": "team1"})
    supabase_service.post("teams", body={"team_name": "Team 2", "lookup": "team2"})

    response = supabase_service.get_all("teams")
    assert len(response) > 0
    assert response[0].get("team_name") == "Team 1"
    assert response[1].get("lookup") == "team2"

    with pytest.raises(TypeError):
        supabase_service.get_all()

    with pytest.raises(HTTPException):
        supabase_service.get_all(None)

    with pytest.raises(HTTPException, match="does not exist"):
        supabase_service.get_all("invalid_table")

def test_supabase_get(supabase_service, clean_teams_table):
    # setup: insert teams
    team_a = supabase_service.post("teams", body={"team_name": "Team A", "lookup": "team_a"})
    team_a_id = team_a.get("team_id")
    team_b = supabase_service.post("teams", body={"team_name": "Team B", "lookup": "team_b"})
    team_b_id = team_b.get("team_id")

    responseA = supabase_service.get_single("teams", id=team_a_id)
    responseB = supabase_service.get_single("teams", id=team_b_id)

    assert responseA.get("team_name") == "Team A"
    assert responseB.get("lookup") == "team_b"
    assert responseB.get("team_id") == team_b_id

    with pytest.raises(HTTPException, match="not found"):
        supabase_service.get_single("teams", id="00000000-0000-0000-0000-000000000000")

def test_supabase_update(supabase_service, clean_teams_table):
    # setup: insert team
    update_team = supabase_service.post("teams", body={"team_name": "UPDATE ME", "lookup": "updateteam"})
    update_team_id = update_team.get("team_id")

    supabase_service.update("teams", body={"team_name": "NEW"}, id=update_team_id)
    response = supabase_service.get_single("teams", id=update_team_id)

    assert response.get("team_name") == "NEW"
    assert response.get("lookup") == "updateteam"

    with pytest.raises(TypeError):
        supabase_service.update()

    with pytest.raises(HTTPException, match="does not exist"):
        supabase_service.update("invalid_table", {"team_name": "TEAM NAME"}, id=update_team_id)

    with pytest.raises(HTTPException, match="cannot be updated"):
        supabase_service.update("teams", body={"team_id": "00000000-0000-0000-0000-000000000000"}, id=update_team_id)

    with pytest.raises(HTTPException, match="null violation"):
        supabase_service.update("teams", body={"team_name": None}, id=update_team_id)

    with pytest.raises(HTTPException, match="not found"):
        supabase_service.update("teams", body={"team_name": "TEAM NAME"}, id="00000000-0000-0000-0000-000000000000")

def test_supabase_delete(supabase_service, clean_teams_table):
    # setup: insert team
    delete_team = supabase_service.post("teams", body={"team_name": "DELETE ME", "lookup": "deleteme"})
    delete_team_id = delete_team.get("team_id")

    delete_response = supabase_service.delete("teams", id=delete_team_id)

    assert delete_response.get("team_id") == delete_team_id
    assert delete_response.get("lookup") == "deleteme" 

    with pytest.raises(TypeError):
        supabase_service.delete()

    with pytest.raises(HTTPException, match="does not exist"):
        supabase_service.delete("invalid_table", id=delete_team_id)

    with pytest.raises(HTTPException, match="not found"):
        supabase_service.get_single("teams", id=delete_team_id)

# helper functions
def test_validate(supabase_service, clean_teams_table):
    # setup: insert team
    supabase_service.post("teams", body={"team_name": "TEST", "lookup": "test"})

    query_api_error = supabase_service.client.table("invalid").select("*")
    with pytest.raises(HTTPException, match="does not exist"):
        validate(query_api_error)

    query_not_found_error = supabase_service.client.table("teams").select("*").eq("team_id", "00000000-0000-0000-0000-000000000000")
    with pytest.raises(HTTPException, match="not found"):
        validate(query_not_found_error)
    
    query = supabase_service.client.table("teams").select("*")
    response = validate(query)
    assert len(response.data) > 0