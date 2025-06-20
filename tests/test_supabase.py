import pytest
from app.utils.supabase import *
from app.utils.env import SUPABASE_TEST_URL, SUPABASE_TEST_API_KEY

def test_supabase_post():
    supabase = SupabaseService(url=SUPABASE_TEST_URL, key=SUPABASE_TEST_API_KEY)
    response = supabase.post("teams", body={"team_name": "TEST TEAM", "lookup": "testteam"})
    assert response.get("team_name") == "TEST TEAM"
    assert response.get("lookup") == "testteam"

# helper functions
def test_table_id():
    assert table_id("users") == "user_id"
    assert table_id("user_availability") == "user_availability_id"

def test_validate_response():
    with pytest.raises(HTTPException):
        validate_response(None)
    
    with pytest.raises(HTTPException):
        validate_response([])