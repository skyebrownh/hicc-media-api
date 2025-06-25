import os
from dotenv import load_dotenv
from app.utils.helpers import table_id

load_dotenv(dotenv_path="test.env", verbose=True)

SUPABASE_TEST_URL = str(os.getenv("SUPABASE_TEST_URL"))
SUPABASE_TEST_API_KEY = str(os.getenv("SUPABASE_TEST_API_KEY"))
FAST_API_KEY = str(os.getenv("FAST_API_KEY"))
BAD_GUID = "99999999-9999-9999-9999-999999999999"

def delete_all(service, table: str):
    value = BAD_GUID

    if table == "dates":
       value = "1900-01-01" 

    service.client.table(table).delete().neq(table_id(table), value).execute()