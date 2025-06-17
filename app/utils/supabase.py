from supabase import create_client, Client

from .env import *

url = SUPABASE_URL
key = SUPABASE_API_KEY
supabase: Client = create_client(url, key)

def supabase_get(table: str, id: str | None = None):
    query = supabase.table(table).select("*")

    if (id):
        query = query.eq(f"{table[0:len(table) - 1] if table.endswith("s") else table}_id", id)

    response = query.execute()
    return response.data

def supabase_post(table: str, body: dict):
    response = supabase.table(table).insert(body).execute()
    return response.data[0]

def supabase_update(table: str, body: dict, id: str):
    response = supabase.table(table).update(body).eq(f"{table[0:len(table) - 1] if table.endswith("s") else table}_id", id).execute()
    print("Update Response", response)
    return response.data[0]

def supabase_delete(table: str, id: str):
    response = supabase.table(table).delete().eq(f"{table[0:len(table) - 1] if table.endswith("s") else table}_id", id).execute()
    return response.data[0]