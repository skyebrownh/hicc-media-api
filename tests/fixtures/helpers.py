from app.utils.helpers import table_id

BAD_GUID = "99999999-9999-9999-9999-999999999999"

def delete_all(service, table: str):
    value = BAD_GUID

    if table == "dates":
       value = "1900-01-01" 

    service.client.table(table).delete().neq(table_id(table), value).execute()