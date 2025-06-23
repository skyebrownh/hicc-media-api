import pytest
from .helpers import delete_all 

USER_PAYLOAD = {"first_name": "TEST", "last_name": "USER", "phone": "1235557890"} 
TEAM_PAYLOAD = {"team_name": "TEST TEAM", "lookup": "testteam"}
TEAM_PAYLOAD2 = {"team_name": "TEAM TWO", "lookup": "teamtwo"}
MEDIA_ROLE_PAYLOAD = {"media_role_name": "TEST MEDIA ROLE", "sort": 10, "lookup": "testmediarole"}
MEDIA_ROLE_PAYLOAD2 = {"media_role_name": "MEDIA ROLE TWO", "sort": 20, "lookup": "mediaroletwo"}
PROFICIENCY_LEVEL_PAYLOAD = {"proficiency_level_name": "TEST PROFICIENCY LEVEL", "lookup": "testproficiencylevel"}
SCHEDULE_DATE_TYPE_PAYLOAD = {"schedule_date_type_name": "TEST SCHEDULE DATE TYPE", "lookup": "testscheduledatetype"}
DATE_PAYLOAD = {"date": "2000-01-01"}
SCHEDULE_PAYLOAD = {"month_start_date": "2000-01-01"}

@pytest.fixture
def setup_user(supabase_service):
    user = supabase_service.post("users", body=USER_PAYLOAD)
    yield user
    delete_all(supabase_service, table="users")

@pytest.fixture
def setup_team(supabase_service):
    team = supabase_service.post("teams", body=TEAM_PAYLOAD)
    yield team
    delete_all(supabase_service, table="teams")

@pytest.fixture
def setup_media_role(supabase_service):
    media_role = supabase_service.post("media_roles", body=MEDIA_ROLE_PAYLOAD)
    yield media_role
    delete_all(supabase_service, table="media_roles")

@pytest.fixture
def setup_proficiency_level(supabase_service):
    proficiency_level = supabase_service.post("proficiency_levels", body=PROFICIENCY_LEVEL_PAYLOAD)
    yield proficiency_level
    delete_all(supabase_service, table="proficiency_levels")

@pytest.fixture
def setup_schedule_date_type(supabase_service):
    schedule_date_type = supabase_service.post("schedule_date_types", body=SCHEDULE_DATE_TYPE_PAYLOAD)
    yield schedule_date_type
    delete_all(supabase_service, table="schedule_date_types")

@pytest.fixture
def setup_date(supabase_service):
    date = supabase_service.post("dates", body=DATE_PAYLOAD)
    yield date
    delete_all(supabase_service, table="dates")

@pytest.fixture
def setup_schedule(supabase_service):
    date = supabase_service.post("dates", body=DATE_PAYLOAD)
    schedule = supabase_service.post("schedules", body=SCHEDULE_PAYLOAD)
    yield schedule
    delete_all(supabase_service, table="schedules")
    delete_all(supabase_service, table="dates")

@pytest.fixture
def setup_user_availability(supabase_service):
    user = supabase_service.post("users", body=USER_PAYLOAD)
    date = supabase_service.post("dates", body=DATE_PAYLOAD)
    ua = supabase_service.post("user_availability", body={"user_id": user.get("user_id"), "date": date.get("date")})
    yield ua, user, date
    delete_all(supabase_service, table="user_availability")
    delete_all(supabase_service, table="dates")
    delete_all(supabase_service, table="users")

@pytest.fixture
def setup_team_user(supabase_service):
    user = supabase_service.post("users", body=USER_PAYLOAD)
    team = supabase_service.post("teams", body=TEAM_PAYLOAD)
    team2 = supabase_service.post("teams", body=TEAM_PAYLOAD2)
    team_user = supabase_service.post("team_users", body={"team_id": team.get("team_id"), "user_id": user.get("user_id")})
    yield team_user, team, user, team2
    delete_all(supabase_service, table="team_users")
    delete_all(supabase_service, table="users")
    delete_all(supabase_service, table="teams")

@pytest.fixture
def setup_user_role(supabase_service):
    user = supabase_service.post("users", body=USER_PAYLOAD)
    media_role = supabase_service.post("media_roles", body=MEDIA_ROLE_PAYLOAD)
    media_role2 = supabase_service.post("media_roles", body=MEDIA_ROLE_PAYLOAD2)
    proficiency_level = supabase_service.post("proficiency_levels", body=PROFICIENCY_LEVEL_PAYLOAD)
    user_role = supabase_service.post("user_roles", body={
        "user_id": user.get("user_id"), 
        "media_role_id": media_role.get("media_role_id"), 
        "proficiency_level_id": proficiency_level.get("proficiency_level_id")
    })
    yield user_role, user, media_role, media_role2
    delete_all(supabase_service, table="user_roles")
    delete_all(supabase_service, table="proficiency_levels")
    delete_all(supabase_service, table="media_roles")
    delete_all(supabase_service, table="users")

@pytest.fixture
def setup_schedule_date(supabase_service):
    schedule = supabase_service.post("schedules", body=SCHEDULE_PAYLOAD)
    date = supabase_service.post("dates", body=DATE_PAYLOAD)
    type = supabase_service.post("schedule_date_types", body=SCHEDULE_DATE_TYPE_PAYLOAD)
    schedule_date = supabase_service.post("schedule_dates", body={
        "schedule_id": schedule.get("schedule_id"),
        "date": date.get("date"),
        "schedule_date_type_id": type.get("schedule_date_type_id")
    })
    yield schedule_date
    delete_all(supabase_service, table="schedule_dates")
    delete_all(supabase_service, table="schedules")
    delete_all(supabase_service, table="dates")
    delete_all(supabase_service, table="schedule_date_type")

@pytest.fixture
def setup_schedule_date_role(supabase_service):
    schedule = supabase_service.post("schedules", body=SCHEDULE_PAYLOAD)
    date = supabase_service.post("dates", body=DATE_PAYLOAD)
    type = supabase_service.post("schedule_date_types", body=SCHEDULE_DATE_TYPE_PAYLOAD)
    schedule_date = supabase_service.post("schedule_dates", body={
        "schedule_id": schedule.get("schedule_id"),
        "date": date.get("date"),
        "schedule_date_type_id": type.get("schedule_date_type_id")
    })
    media_role = supabase_service.post("media_role", body=MEDIA_ROLE_PAYLOAD)
    schedule_date_role = supabase_service.post("schedule_date_roles", body={
        "schedule_date_id": schedule_date.get("schedule_date_id"),
        "media_role_id": media_role.get("media_role_id")
    })
    yield schedule_date_role