import pytest
from app.utils.supabase import *

def test_table_id():
    assert table_id("users") == "user_id"
    assert table_id("user_availability") == "user_availability_id"

def test_validate_response():
    with pytest.raises(HTTPException):
        validate_response(None)
    
    with pytest.raises(HTTPException):
        validate_response([])