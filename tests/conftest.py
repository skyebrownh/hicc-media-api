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
def clean_teams_table(supabase_service):
    supabase_service.client.table("teams").delete().neq("team_id", "99999999-9999-9999-9999-999999999999").execute() # delete all teams
    yield
    supabase_service.client.table("teams").delete().neq("team_id", "99999999-9999-9999-9999-999999999999").execute()

@pytest.fixture
def test_client(supabase_service):
    app.dependency_overrides[get_supabase_service] = lambda: supabase_service
    with TestClient(app) as client:
        yield client
    app.dependency_overrides = {} # cleans state after test

@pytest.fixture
def setup_user(supabase_service):
    # insert test user
    user = supabase_service.post("users", body={"first_name": "TEST", "last_name": "USER", "phone": "1235557890"})

    # make available to tests
    yield user

    # clean up after tests
    supabase_service.delete("users", user.get("user_id"))

@pytest.fixture
def clean_users_table(supabase_service):
    supabase_service.client.table("users").delete().neq("user_id", "99999999-9999-9999-9999-999999999999").execute() # delete all users
    yield
    supabase_service.client.table("users").delete().neq("user_id", "99999999-9999-9999-9999-999999999999").execute()