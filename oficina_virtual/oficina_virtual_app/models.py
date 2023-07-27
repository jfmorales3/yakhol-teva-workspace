from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    username = None  # Elimina el campo de nombre de usuario
    email = models.EmailField('Correo electrónico', unique=True)  # Haz que el correo electrónico sea único
    user_type = models.PositiveSmallIntegerField(choices=[(1, 'admin'), (2, 'comercial'), (3, 'asociado')], default=1)

    objects = CustomUserManager()  # Usa el manager personalizado

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Django espera la lista de los campos que serán solicitados al crear un usuario, aparte del USERNAME_FIELD.

    def __str__(self):
        return self.email

class Comercial(models.Model):
    identificacion = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    correo = models.EmailField()
    ciudad = models.CharField(max_length=200)
    lider = models.ForeignKey('self', on_delete=models.SET_NULL, null=True)

class Contrato(models.Model):
    id_contrato = models.CharField(max_length=200, primary_key=True)
    tipo_contrato = models.CharField(max_length=200)
    id_asociado = models.ForeignKey('Asociado', on_delete=models.CASCADE)
    tipo_semana = models.ForeignKey('TipoSemana', on_delete=models.CASCADE)
    id_comercial = models.ForeignKey('Comercial', on_delete=models.CASCADE)
    valor_semana = models.IntegerField()
    valor_pagado = models.IntegerField()
    saldo_restante = models.IntegerField()
    semana = models.CharField(max_length=200)

class Pago(models.Model):
    rc = models.IntegerField(primary_key=True)
    id_contrato = models.ForeignKey('Contrato', on_delete=models.CASCADE)
    fecha_pago = models.DateField()
    destino = models.CharField(max_length=200)
    valor = models.IntegerField()
    cuota_administrativa = models.IntegerField()
    numero_cuenta = models.CharField(max_length=200)
    tipo_pago = models.CharField(max_length=200)
    pagos_id = models.IntegerField()
    asociado = models.ForeignKey('Asociado', on_delete=models.CASCADE, related_name='pagos_rel')




class Comision(models.Model):
    id = models.AutoField(primary_key=True)
    comercial = models.ForeignKey('Comercial', on_delete=models.CASCADE)
    contrato = models.ForeignKey('Contrato', on_delete=models.CASCADE)
    nivel = models.IntegerField()
    valor_efectivo = models.IntegerField()
    valor_tokens = models.IntegerField()

class Asociado(models.Model):
    numero_documento = models.IntegerField(primary_key=True)
    tipo_documento = models.CharField(max_length=200)
    lugar_expedicion = models.CharField(max_length=200)
    nombre_completo = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)
    correo = models.EmailField()
    ocupacion = models.CharField(max_length=200)
    contratos = models.ManyToManyField('Contrato')
    pagos = models.ManyToManyField('Pago', related_name='asociados_rel')
    tipo_semana = models.ForeignKey('TipoSemana', on_delete=models.CASCADE)
    tipo_asociado = models.CharField(max_length=200)
    last_modified = models.DateTimeField()
    deuda_total = models.IntegerField()

class TipoSemana(models.Model):
    id = models.IntegerField(primary_key=True)
    tipo_semana = models.CharField(max_length=200)
    valor = models.IntegerField()
    contratos = models.ManyToManyField('Contrato')
    asociados = models.IntegerField()