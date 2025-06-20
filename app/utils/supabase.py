from fastapi import HTTPException
from supabase import create_client, Client

class SupabaseService():
    def __init__(self, url, key):
        self.client: Client = create_client(url, key)

    def get(self, table: str, id: str | None = None):
        query = self.client.table(table).select("*")

        if id:
            query = query.eq(table_id(table), id)

        response = query.execute()
        validate_response(response)
        return response.data

    def post(self, table: str, body: dict):
        response = self.client.table(table).insert(body).execute()
        validate_response(response)
        return response.data[0]

    def update(self, table: str, body: dict, id: str):
        response = self.client.table(table).update(body).eq(table_id(table), id).execute()
        validate_response(response)
        return response.data[0]

    def delete(self, table: str, id: str):
        response = self.client.table(table).delete().eq(table_id(table), id).execute()
        validate_response(response)
        return response.data[0]

# helper functions
def table_id(table: str) -> str:
    return f"{table[0:len(table) - 1] if table.endswith("s") else table}_id"

def validate_response(response):
    if not response or len(response.data) == 0:
        raise HTTPException(status_code=404, detail="Resource Not Found")