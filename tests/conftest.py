import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.utils.supabase import SupabaseService
from app.utils.env import SUPABASE_TEST_URL, SUPABASE_TEST_API_KEY
from app.dependencies import get_supabase_service 

BAD_GUID = "99999999-9999-9999-9999-999999999999"

@pytest.fixture(scope="session")
def supabase_service():
    return SupabaseService(url=SUPABASE_TEST_URL, key=SUPABASE_TEST_API_KEY)

@pytest.fixture
def test_client(supabase_service):
    app.dependency_overrides[get_supabase_service] = lambda: supabase_service
    with TestClient(app) as client:
        yield client
    app.dependency_overrides = {} # cleans state after test

# clean table fixtures
@pytest.fixture
def clean_users_table(supabase_service):
    supabase_service.client.table("users").delete().neq("user_id", BAD_GUID).execute()
    yield
    supabase_service.client.table("users").delete().neq("user_id", BAD_GUID).execute()

@pytest.fixture
def clean_teams_table(supabase_service):
    supabase_service.client.table("teams").delete().neq("team_id", BAD_GUID).execute()
    yield
    supabase_service.client.table("teams").delete().neq("team_id", BAD_GUID).execute()

@pytest.fixture
def clean_media_roles_table(supabase_service):
    supabase_service.client.table("media_roles").delete().neq("media_role_id", BAD_GUID).execute()
    yield
    supabase_service.client.table("media_roles").delete().neq("media_role_id", BAD_GUID).execute()

@pytest.fixture
def clean_proficiency_levels_table(supabase_service):
    supabase_service.client.table("proficiency_levels").delete().neq("proficiency_level_id", BAD_GUID).execute()
    yield
    supabase_service.client.table("proficiency_levels").delete().neq("proficiency_level_id", BAD_GUID).execute()

@pytest.fixture
def clean_schedule_date_types_table(supabase_service):
    supabase_service.client.table("schedule_date_types").delete().neq("schedule_date_type_id", BAD_GUID).execute()
    yield
    supabase_service.client.table("schedule_date_types").delete().neq("schedule_date_type_id", BAD_GUID).execute()

@pytest.fixture
def clean_dates_table(supabase_service):
    supabase_service.client.table("dates").delete().neq("date", "1900-01-01").execute()
    yield
    supabase_service.client.table("dates").delete().neq("date", "1900-01-01").execute()

# setup fixtures
@pytest.fixture
def setup_user(supabase_service):
    user = supabase_service.post("users", body={"first_name": "TEST", "last_name": "USER", "phone": "1235557890"})
    yield user
    supabase_service.client.table("users").delete().neq("user_id", BAD_GUID).execute()

@pytest.fixture
def setup_team(supabase_service):
    team = supabase_service.post("teams", body={"team_name": "TEST TEAM", "lookup": "testteam"})
    yield team
    supabase_service.client.table("teams").delete().neq("team_id", BAD_GUID).execute()

@pytest.fixture
def setup_media_role(supabase_service):
    media_role = supabase_service.post("media_roles", body={"media_role_name": "TEST MEDIA ROLE", "sort": 10, "lookup": "testmediarole"})
    yield media_role
    supabase_service.client.table("media_roles").delete().neq("media_role_id", BAD_GUID).execute()

@pytest.fixture
def setup_proficiency_level(supabase_service):
    proficiency_level = supabase_service.post("proficiency_levels", body={"proficiency_level_name": "TEST PROFICIENCY LEVEL", "lookup": "testproficiencylevel"})
    yield proficiency_level
    supabase_service.client.table("proficiency_levels").delete().neq("proficiency_level_id", BAD_GUID).execute()

@pytest.fixture
def setup_schedule_date_type(supabase_service):
    schedule_date_type = supabase_service.post("schedule_date_types", body={"schedule_date_type_name": "TEST SCHEDULE DATE TYPE", "lookup": "testscheduledatetype"})
    yield schedule_date_type
    supabase_service.client.table("schedule_date_types").delete().neq("schedule_date_type_id", BAD_GUID).execute()

@pytest.fixture
def setup_date(supabase_service):
    date = supabase_service.post("dates", body={"date": "2000-01-01"})
    yield date
    supabase_service.client.table("dates").delete().neq("date", "1900-01-01").execute()