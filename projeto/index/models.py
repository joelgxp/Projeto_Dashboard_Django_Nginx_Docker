import uuid
import os

from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_image_file_extension
from localflavor.br.models import BRCPFField


def nome_arquivo_foto(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid.uuid4(), ext)
    
    return os.path.join('usuarios_fotos', filename)

def nome_arquivo_documento(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid.uuid4(), ext)
    
    return os.path.join('documentos_fotos', filename)

class Usuario(AbstractUser):
    TIPO_USUARIO_CHOICES = (
        (1, 'Lider'),
        (2, 'Colaborador')
    )
    
    nome_completo = models.CharField(max_length=200, null=False, blank=False)
    cpf = BRCPFField(null=False, blank=True)
    nascimento = models.DateField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False, unique=True)
    celular = models.CharField(max_length=15, null=False, blank=False)
    tipp_usuario = models.CharField(max_length=1, choices=TIPO_USUARIO_CHOICES, null=False, blank=False)
    foto_de_perfil = models.ImageField(upload_to=nome_arquivo_foto, null=False, validators = [validate_image_file_extension, ])
    foto_documento = models.ImageField(upload_to=nome_arquivo_documento, null=False, validators=[validate_image_file_extension, ])    
    ativo = models.BooleanField(default=True)
    
class LiderModel(models.Model):
    nome = models.CharField(max_length=255)
    departamento = models.CharField(max_length=255)
    email = models.EmailField()
    senha = models.CharField(max_length=255)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nome} - {self.email} - {self.departamento}"
    
class LiderForm(forms.ModelForm):
    class Meta:
        model = LiderModel
        fields = ['nome', 'departamento', 'email', 'senha']
