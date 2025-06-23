import pytest
from .helpers import delete_all

@pytest.fixture
def clean_users_table(supabase_service):
    delete_all(supabase_service, table="users")
    yield
    delete_all(supabase_service, table="users")

@pytest.fixture
def clean_teams_table(supabase_service):
    delete_all(supabase_service, table="teams")
    yield
    delete_all(supabase_service, table="teams")

@pytest.fixture
def clean_media_roles_table(supabase_service):
    delete_all(supabase_service, table="media_roles")
    yield
    delete_all(supabase_service, table="media_roles")

@pytest.fixture
def clean_proficiency_levels_table(supabase_service):
    delete_all(supabase_service, table="proficiency_levels")
    yield
    delete_all(supabase_service, table="proficiency_levels")

@pytest.fixture
def clean_schedule_date_types_table(supabase_service):
    delete_all(supabase_service, table="schedule_date_types")
    yield
    delete_all(supabase_service, table="schedule_date_types")

@pytest.fixture
def clean_dates_table(supabase_service):
    delete_all(supabase_service, table="dates")
    yield
    delete_all(supabase_service, table="dates")

@pytest.fixture
def clean_schedules_table(supabase_service):
    delete_all(supabase_service, table="schedules")
    yield
    delete_all(supabase_service, table="schedules")
    
@pytest.fixture
def clean_user_availability_table(supabase_service):
    delete_all(supabase_service, table="user_availability")
    yield
    delete_all(supabase_service, table="user_availability")

@pytest.fixture
def clean_team_users_table(supabase_service):
    delete_all(supabase_service, table="team_users")
    yield
    delete_all(supabase_service, table="team_users")

@pytest.fixture
def clean_user_roles_table(supabase_service):
    delete_all(supabase_service, "user_roles")
    yield
    delete_all(supabase_service, "user_roles")

@pytest.fixture
def clean_schedule_dates_table(supabase_service):
    delete_all(supabase_service, table="schedule_dates")
    yield
    delete_all(supabase_service, table="schedule_dates")

@pytest.fixture
def clean_schedule_date_roles_table(supabase_service):
    delete_all(supabase_service, table="schedule_date_roles")
    yield
    delete_all(supabase_service, table="schedule_date_roles")