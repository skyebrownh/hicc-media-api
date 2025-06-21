from fastapi import HTTPException
from supabase import create_client, Client, PostgrestAPIError

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
        if table_id(table) in body:
            raise HTTPException(status_code=400, detail="Primary Key/ID cannot be updated")

        query = self.client.table(table).update(body).eq(table_id(table), id)
        response = validate(query)
        return response.data[0]

    def delete(self, table: str, id: str):
        query = self.client.table(table).delete().eq(table_id(table), id)
        response = validate(query)
        return response.data[0]

# helper functions
def table_id(table: str) -> str:
    return f"{table[0:len(table) - 1] if table.endswith("s") else table}_id"

def validate(query):
    try:
        response = query.execute()
    except PostgrestAPIError:
        raise HTTPException(status_code=500, detail="API Error occurred")

    if not response or len(response.data) == 0:
        raise HTTPException(status_code=404, detail="Resource Not Found")
    
    return response