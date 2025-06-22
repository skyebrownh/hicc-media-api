import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.utils.supabase import SupabaseService
from app.utils.env import SUPABASE_TEST_URL, SUPABASE_TEST_API_KEY
from app.dependencies import get_supabase_service 

@pytest.fixture(scope="session")
def supabase_service():
    return SupabaseService(url=SUPABASE_TEST_URL, key=SUPABASE_TEST_API_KEY)

@pytest.fixture
def test_client(supabase_service):
    app.dependency_overrides[get_supabase_service] = lambda: supabase_service
    with TestClient(app) as client:
        yield client
    app.dependency_overrides = {} # cleans state after test

@pytest.fixture
def clean_users_table(supabase_service):
    supabase_service.client.table("users").delete().neq("user_id", "99999999-9999-9999-9999-999999999999").execute()
    yield
    supabase_service.client.table("users").delete().neq("user_id", "99999999-9999-9999-9999-999999999999").execute()

@pytest.fixture
def clean_teams_table(supabase_service):
    supabase_service.client.table("teams").delete().neq("team_id", "99999999-9999-9999-9999-999999999999").execute()
    yield
    supabase_service.client.table("teams").delete().neq("team_id", "99999999-9999-9999-9999-999999999999").execute()

@pytest.fixture
def setup_user(supabase_service):
    user = supabase_service.post("users", body={"first_name": "TEST", "last_name": "USER", "phone": "1235557890"})
    yield user
    supabase_service.client.table("users").delete().neq("user_id", "99999999-9999-9999-9999-999999999999").execute()

@pytest.fixture
def setup_team(supabase_service):
    team = supabase_service.post("teams", body={"team_name": "TEST TEAM", "lookup": "testteam"})
    yield team
    supabase_service.client.table("teams").delete().neq("team_id", "99999999-9999-9999-9999-999999999999").execute()