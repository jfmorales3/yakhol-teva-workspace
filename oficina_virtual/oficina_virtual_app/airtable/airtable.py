from airtable import Airtable

# tus claves
base_key = 'apptkevjIOV2QLtos'
api_key = 'keyMxHRVe4JVxyanz'

# Inicializa las tablas
airtable_comerciales = Airtable(base_key, 'tblTPSfrSDPUGZfzX', api_key)
airtable_contratos = Airtable(base_key, 'tbl8U1YcYv0qqrn9g', api_key)
airtable_pagos = Airtable(base_key, 'tbl0kMNkGmsK2NBd8', api_key)
airtable_comisiones = Airtable(base_key, 'tblxZVgXcMHSyTToO', api_key)
airtable_asociados = Airtable(base_key, 'tblX74Op1WB61ITkE', api_key)
airtable_tipos_de_semanas = Airtable(base_key, 'tblKhPPvuHsbeLFHe', api_key)
