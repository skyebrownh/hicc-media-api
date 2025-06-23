import pytest
from app.utils.helpers import *

def test_table_id():
    assert table_id("users") == "user_id"
    assert table_id("schedule_date_types") == "schedule_date_type_id"
    assert table_id("user_availability") == "user_availability_id"
    assert table_id("dates") == "date"