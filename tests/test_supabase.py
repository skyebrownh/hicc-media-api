from app.utils.supabase import *

def test_table_id():
    table_id1 = table_id("users")
    table_id2 = table_id("user_availability")

    assert table_id1 == "user_id"
    assert table_id2 == "user_availability_id"