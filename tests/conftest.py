import pytest
from app.utils.supabase import SupabaseService
from app.utils.env import SUPABASE_TEST_URL, SUPABASE_TEST_API_KEY

@pytest.fixture(scope="session")
def supabase_service():
    return SupabaseService(url=SUPABASE_TEST_URL, key=SUPABASE_TEST_API_KEY)

@pytest.fixture()
def clean_teams_table(supabase_service):
    supabase_service.client.table("teams").delete().neq("team_id", "00000000-0000-0000-0000-000000000000").execute() # delete all teams
    yield
    supabase_service.client.table("teams").delete().neq("team_id", "00000000-0000-0000-0000-000000000000").execute()