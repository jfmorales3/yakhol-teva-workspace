from .airtable import airtable_comerciales

def get_comercial_by_id(identificacion):
    match = airtable_comerciales.search('Identificación', identificacion)
    if match:
        return match[0]['fields']
    else:
        return None

def get_comercial_by_email(email):
    match = airtable_comerciales.search('Correo', email)
    if match:
        return match[0]['fields']
    else:
        return None

def update_comercial_by_id(identificacion, updated_info):
    record = airtable_comerciales.search('Identificación', identificacion)
    if record:
        airtable_comerciales.update(record[0]['id'], updated_info)
        return True
    else:
        return False

def update_comercial_by_email(email, updated_info):
    record = airtable_comerciales.search('Correo', email)
    if record:
        airtable_comerciales.update(record[0]['id'], updated_info)
        return True
    else:
        return False
