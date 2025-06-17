from supabase import create_client, Client

from .env import *

url = SUPABASE_URL
key = SUPABASE_API_KEY
supabase: Client = create_client(url, key)

def supabase_get(table: str):
    return supabase.table(table).select("*").execute()

def supabase_post(table: str, body: dict):
    return supabase.table(table).insert(body).execute()

def supabase_update(table: str, body: dict, id: str):
    return supabase.table(table).update(body).eq(f"{table[0:len(table) - 1] if table.endswith("s") else table}_id", id).execute()

def supabase_delete(table: str):
    return supabase.table(table).delete().eq(f"{table[0:len(table) - 1] if table.endswith("s") else table}_id", id).execute()