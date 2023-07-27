from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Comercial, Contrato, Pago, Comision, Asociado, TipoSemana

# Define una clase personalizada para el modelo 'CustomUser' en el panel de administración
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'user_type'),
        }),
    )
    fieldsets = (
        (None, {'fields': ('email', 'password', 'user_type')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('email', 'user_type', 'is_staff', 'is_active',)
    list_filter = ('is_staff', 'is_active', 'user_type',)
    search_fields = ('email',)
    ordering = ('email',)

# Define una clase personalizada para el modelo 'Comercial' en el panel de administración
class ComercialAdmin(admin.ModelAdmin):
    list_display = ('identificacion', 'nombre', 'telefono', 'correo', 'ciudad', 'lider')
    list_filter = ('ciudad', )
    search_fields = ('nombre', 'correo')

# Define una clase personalizada para el modelo 'Contrato' en el panel de administración
class ContratoAdmin(admin.ModelAdmin):
    list_display = ('id_contrato', 'tipo_contrato', 'id_asociado', 'tipo_semana', 'id_comercial', 'valor_semana', 'valor_pagado', 'saldo_restante', 'semana')
    list_filter = ('tipo_contrato', 'semana')
    search_fields = ('id_contrato', 'id_asociado__nombre')  # Permite buscar por ID del contrato o nombre del asociado

# Define una clase personalizada para el modelo 'Pago' en el panel de administración
class PagoAdmin(admin.ModelAdmin):
    list_display = ('rc', 'id_contrato', 'fecha_pago', 'destino', 'valor', 'cuota_administrativa', 'numero_cuenta', 'tipo_pago', 'pagos_id', 'asociado')
    list_filter = ('fecha_pago', 'destino')
    search_fields = ('rc', 'id_contrato__id_contrato', 'asociado__nombre_completo')  # Permite buscar por RC, ID del contrato o nombre del asociado

# Define una clase personalizada para el modelo 'Comision' en el panel de administración
class ComisionAdmin(admin.ModelAdmin):
    list_display = ('id', 'comercial', 'contrato', 'nivel', 'valor_efectivo', 'valor_tokens')
    list_filter = ('nivel', )
    search_fields = ('id', 'comercial__nombre', 'contrato__id_contrato')  # Permite buscar por ID, nombre del comercial o ID del contrato

# Define una clase personalizada para el modelo 'Asociado' en el panel de administración
class AsociadoAdmin(admin.ModelAdmin):
    list_display = ('numero_documento', 'tipo_documento', 'nombre_completo', 'telefono', 'correo', 'ciudad', 'tipo_asociado', 'last_modified')
    list_filter = ('tipo_asociado', 'ciudad')
    search_fields = ('numero_documento', 'nombre_completo', 'correo')

# Define una clase personalizada para el modelo 'TipoSemana' en el panel de administración
class TipoSemanaAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo_semana', 'valor', 'asociados')
    list_filter = ('valor', )
    search_fields = ('tipo_semana', )

# Registra los modelos personalizados en el panel de administración
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Comercial, ComercialAdmin)
admin.site.register(Contrato, ContratoAdmin)
admin.site.register(Pago, PagoAdmin)
admin.site.register(Comision, ComisionAdmin)
admin.site.register(Asociado, AsociadoAdmin)
admin.site.register(TipoSemana, TipoSemanaAdmin)
