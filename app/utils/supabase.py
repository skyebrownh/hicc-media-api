from fastapi import HTTPException
from supabase import create_client, Client

from .env import SUPABASE_URL, SUPABASE_API_KEY 

url = SUPABASE_URL
key = SUPABASE_API_KEY
supabase: Client = create_client(url, key)

def supabase_get(table: str, id: str | None = None):
    query = supabase.table(table).select("*")

    if id:
        query = query.eq(table_id(table), id)

    response = query.execute()
    validate_response(response)
    return response.data

def supabase_post(table: str, body: dict):
    response = supabase.table(table).insert(body).execute()
    validate_response(response)
    return response.data[0]

def supabase_update(table: str, body: dict, id: str):
    response = supabase.table(table).update(body).eq(table_id(table), id).execute()
    validate_response(response)
    return response.data[0]

def supabase_delete(table: str, id: str):
    response = supabase.table(table).delete().eq(table_id(table), id).execute()
    validate_response(response)
    return response.data[0]

# helper functions
def table_id(table: str) -> str:
    return f"{table[0:len(table) - 1] if table.endswith("s") else table}_id"

def validate_response(response):
    if not response or len(response.data) == 0:
        raise HTTPException(status_code=404, detail="Resource Not Found")