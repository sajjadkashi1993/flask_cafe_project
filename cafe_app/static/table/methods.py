import json

def get_all_table_info(tables):
    full_info = []
    for table in tables:
        table_info = {
            "id": table.id,
            "table-number": table.table_number,
            "position": table.position,
            "seater": table.table_spacing,
            }
        full_info.append(table_info)
    result = json.dumps(full_info)
    return result