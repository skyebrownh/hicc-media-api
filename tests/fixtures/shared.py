import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.utils.supabase import SupabaseService
from app.utils.env import SUPABASE_TEST_URL, SUPABASE_TEST_API_KEY
from app.dependencies import get_supabase_service 

__all__ = [
    "supabase_service",
    "test_client"
]

@pytest.fixture(scope="session")
def supabase_service():
    return SupabaseService(url=SUPABASE_TEST_URL, key=SUPABASE_TEST_API_KEY)

@pytest.fixture
def test_client(supabase_service):
    app.dependency_overrides[get_supabase_service] = lambda: supabase_service
    with TestClient(app) as client:
        yield client
    app.dependency_overrides = {} # cleans state after test