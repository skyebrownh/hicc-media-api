def table_id(table: str) -> str:
    if table == "dates":
        return "date"

    return f"{table[0:len(table) - 1] if table.endswith("s") else table}_id"