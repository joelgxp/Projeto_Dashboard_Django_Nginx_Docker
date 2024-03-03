from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    nome = models.CharField(max_length=255)    
    ativo = models.BooleanField(default=True)
    
    REQUIRED_FIELDS = ['email', 'password']

    def __str__(self):
        return f"{self.username, self.email, self.password, self.last_login, self.is_superuser, self.is_staff, self.is_active, self.date_joined, self.ativo}"