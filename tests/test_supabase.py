import pytest
from app.utils.supabase import *

def test_supabase_post(supabase_service, clean_teams_table):
    response = supabase_service.post("teams", body={"team_name": "TEST TEAM", "lookup": "testteam"})
    assert response.get("team_name") == "TEST TEAM"
    assert response.get("lookup") == "testteam"

def test_supabase_get_all(supabase_service, clean_teams_table):
    # setup: insert teams
    supabase_service.post("teams", body={"team_name": "Team 1", "lookup": "team1"})
    supabase_service.post("teams", body={"team_name": "Team 2", "lookup": "team2"})

    response = supabase_service.get("teams")
    assert len(response) > 0
    assert response[0].get("team_name") == "Team 1"
    assert response[1].get("lookup") == "team2"

def test_supabase_get(supabase_service, clean_teams_table):
    # setup: insert teams
    teamA = supabase_service.post("teams", body={"team_name": "Team A", "lookup": "teamA"})
    teamB = supabase_service.post("teams", body={"team_name": "Team B", "lookup": "teamB"})

    responseA = supabase_service.get("teams", id=teamA.get("team_id"))
    responseB = supabase_service.get("teams", id=teamB.get("team_id"))

    assert responseA[0].get("team_name") == "Team A"
    assert responseB[0].get("lookup") == "teamB"
    assert responseB[0].get("team_id") == teamB.get("team_id")

# helper functions
def test_table_id():
    assert table_id("users") == "user_id"
    assert table_id("user_availability") == "user_availability_id"

def test_validate_response():
    with pytest.raises(HTTPException):
        validate_response(None)
    
    with pytest.raises(HTTPException):
        validate_response([])