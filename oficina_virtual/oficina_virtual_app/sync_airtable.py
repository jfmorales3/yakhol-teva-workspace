import time
from datetime import datetime
from .models import Comercial, Contrato, Pago, Comision, Asociado, TipoSemana
from .airtable import airtable_comerciales, airtable_contratos, airtable_pagos, airtable_comisiones, airtable_asociados, airtable_tipos_de_semanas

def sync_airtable():
    last_sync_time = datetime.now()

    while True:
        try:
            # Descarga los datos de Airtable que han sido modificados desde la última sincronización
            comerciales_data = airtable_comerciales.get_all(formula=f"LAST_MODIFIED_TIME > '{last_sync_time.isoformat()}'")
            contratos_data = airtable_contratos.get_all(formula=f"LAST_MODIFIED_TIME > '{last_sync_time.isoformat()}'")
            pagos_data = airtable_pagos.get_all(formula=f"LAST_MODIFIED_TIME > '{last_sync_time.isoformat()}'")
            comisiones_data = airtable_comisiones.get_all(formula=f"LAST_MODIFIED_TIME > '{last_sync_time.isoformat()}'")
            asociados_data = airtable_asociados.get_all(formula=f"LAST_MODIFIED_TIME > '{last_sync_time.isoformat()}'")
            tipos_de_semanas_data = airtable_tipos_de_semanas.get_all(formula=f"LAST_MODIFIED_TIME > '{last_sync_time.isoformat()}'")

            # Almacena los datos en la base de datos local
            for comercial_data in comerciales_data:
                Comercial.objects.update_or_create(
                    identificacion=comercial_data['fields']['Identificación'],
                    defaults={
                        'nombre': comercial_data['fields']['Nombre'],
                        'telefono': comercial_data['fields']['Teléfono'],
                        'correo': comercial_data['fields']['Correo'],
                        'ciudad': comercial_data['fields']['Ciudad'],
                        'lider_id': comercial_data['fields']['Lider'][0] if comercial_data['fields']['Lider'] else None,
                    }
                )

            for contrato_data in contratos_data:
                Contrato.objects.update_or_create(
                    id_contrato=contrato_data['fields']['ID CONTRATO'],
                    defaults={
                        'tipo_contrato': contrato_data['fields']['TIPO CONTRATO'],
                        'id_asociado_id': contrato_data['fields']['ID ASOCIADO'][0],
                        'tipo_semana_id': contrato_data['fields']['Tipo de semana'][0],
                        'id_comercial_id': contrato_data['fields']['ID Comercial'][0],
                        'valor_semana': contrato_data['fields']['Valor Semana'],
                        'valor_pagado': contrato_data['fields']['Valor pagado'],
                        'saldo_restante': contrato_data['fields']['Saldo restante'],
                        'semana': contrato_data['fields']['Semana'],
                    }
                )

            for pago_data in pagos_data:
                Pago.objects.update_or_create(
                    rc=pago_data['fields']['RC'],
                    defaults={
                        'id_contrato_id': pago_data['fields']['ID CONTRATO'][0],
                        'fecha_pago': pago_data['fields']['Fecha de pago'],
                        'destino': pago_data['fields']['Destino'],
                        'valor': pago_data['fields']['Valor'],
                        'cuota_administrativa': pago_data['fields']['Cuota Administrativa'],
                        'numero_cuenta': pago_data['fields']['Número de cuenta'],
                        'tipo_pago': pago_data['fields']['TIPO DE PAGO'],
                        'pagos_id': pago_data['fields']['Pagos ID'],
                        'asociado_id': pago_data['fields']['Asociado'][0],
                    }
                )

            for comision_data in comisiones_data:
                Comision.objects.update_or_create(
                    id=comision_data['id'],
                    defaults={
                        'comercial_id': comision_data['fields']['Comercial'][0],
                        'contrato_id': comision_data['fields']['Contrato'][0],
                        'nivel': comision_data['fields']['Nivel'],
                        'valor_efectivo': comision_data['fields']['Valor Efectivo'],
                        'valor_tokens': comision_data['fields']['Valor Tokens'],
                    }
                )

            for asociado_data in asociados_data:
                Asociado.objects.update_or_create(
                    numero_documento=asociado_data['fields']['Número de documento'],
                    defaults={
                        'tipo_documento': asociado_data['fields']['Tipo de documento'],
                        'lugar_expedicion': asociado_data['fields']['Lugar de expedición'],
                        'nombre_completo': asociado_data['fields']['Nombre Completo'],
                        'telefono': asociado_data['fields']['Teléfono'],
                        'direccion': asociado_data['fields']['Dirección'],
                        'ciudad': asociado_data['fields']['Ciudad'],
                        'correo': asociado_data['fields']['Correo'],
                        'ocupacion': asociado_data['fields']['Ocupación'],
                        'tipo_semana_id': asociado_data['fields']['Tipo de semana'][0],
                        'tipo_asociado': asociado_data['fields']['Tipo de Asociado'],
                        'last_modified': asociado_data['fields']['Last Modified'],
                        'deuda_total': asociado_data['fields']['Deuda total'],
                    }
                )

            for tipo_semana_data in tipos_de_semanas_data:
                TipoSemana.objects.update_or_create(
                    id=tipo_semana_data['fields']['ID'],
                    defaults={
                        'tipo_semana': tipo_semana_data['fields']['Tipo de semana'],
                        'valor': tipo_semana_data['fields']['Valor'],
                        'asociados': tipo_semana_data['fields']['Asociados'],
                    }
                )

            # Actualiza el tiempo de la última sincronización
            last_sync_time = datetime.now()

        except Exception as e:
            print(f"Error durante la sincronización: {e}")

        finally:
            # Espera 30 segundos antes de la próxima actualización
            time.sleep(30)
