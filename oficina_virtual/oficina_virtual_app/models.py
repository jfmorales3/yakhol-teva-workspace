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
