from fastapi import HTTPException
from supabase import create_client, Client, PostgrestAPIError

from app.utils.helpers import table_id

class SupabaseService():
    def __init__(self, url, key):
        self.client: Client = create_client(url, key)

    def get(self, table: str, id: str | None = None):
        query = self.client.table(table).select("*")

        if id:
            query = query.eq(table_id(table), id)
        
        response = validate(query)
        return response.data

    def post(self, table: str, body: dict):
        query = self.client.table(table).insert(body)
        response = validate(query)
        return response.data[0]

    def update(self, table: str, body: dict, id: str):
        # only applies to direct calls, not through FastAPI
        if table_id(table) in body:
            raise HTTPException(status_code=400, detail="Primary Key/ID cannot be updated")

        query = self.client.table(table).update(body).eq(table_id(table), id)
        response = validate(query)
        return response.data[0]

    def delete(self, table: str, id: str):
        query = self.client.table(table).delete().eq(table_id(table), id)
        response = validate(query)
        return response.data[0]

def validate(query):
    try:
        response = query.execute()
    except PostgrestAPIError as e:
        print("🔥 Supabase error:", e.message)
        raise HTTPException(status_code=500, detail=f"API Error: {e.message}")

    if not response or len(response.data) == 0:
        raise HTTPException(status_code=404, detail="Resource Not Found")
    
    return response