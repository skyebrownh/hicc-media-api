from supabase import create_client, Client

from .env import *

url = SUPABASE_URL
key = SUPABASE_API_KEY
supabase: Client = create_client(url, key)

def supabase_get(table: str):
    return supabase.table(table).select("*").execute()