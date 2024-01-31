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

class PacienteModel(models.Model):
    CATEGORIA_CHOICES = (
        ('A', "A"),
        ('B', "B"),
        ('C', "C"),
        ('D', "D"),
        ('E', "E"),
        ('AB', "AB"),       
        ('AC', "AC"),
        ('AD', "AD"),
        ('AE', "AE")
    )
    SOLICITACAO_CHOICES = (
        ('PRIMEIRA_HABILITACAO', "Primeira Habilitação"),
        ('RENOVACAO', "Renovação"),
        ('ADICAO_CATEGORIA', "Adição de Categoria"),
        ('MUDANCA_CATEGORIA', "Mudança de Categoria")
    )
    SEXO_CHOICES = (
        ('MASCULINO', "Masculino"),
        ('FEMININO', "Feminino")
    )
    
    guia = models.IntegerField(null=False, blank=False)
    registro = models.IntegerField(null=False, blank=False)
    categoria = models.CharField(max_length=5, choices=CATEGORIA_CHOICES, null=False, blank=False)
    solicitacao = models.CharField(max_length=25, choices=SOLICITACAO_CHOICES, null=False, blank=False)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_habilitacao = models.DateField(null=False, blank=False)
    nome_completo = models.CharField(max_length=200, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    sexo = models.CharField(max_length=25, choices=SEXO_CHOICES, null=False, blank=False)
    identidade = models.CharField(max_length=25, null=False, blank=False)
    orgao_emissor = models.CharField(max_length=25, null=False, blank=False)
    uf_emissor = models.CharField(max_length=25, null=False, blank=False)
    naturalidade = models.CharField(max_length=45, null=False, blank=False)
    uf_naturalidade = models.CharField(max_length=25, null=False, blank=False)
    
    nome_mae = models.CharField(max_length=200, null=False, blank=False)
    nome_pai = models.CharField(max_length=200, null=False, blank=False)
    celular = models.CharField(max_length=15, null=False, blank=False)
    cpf = BRCPFField(null=False, blank=True)
    logradouro = models.CharField(max_length=200, null=False, blank=False)
    numero = models.CharField(max_length=10, null=False, blank=False)
    bairro = models.CharField(max_length=45, null=False, blank=False)
    cidade = models.CharField(max_length=45, null=False, blank=False)
    cep = models.CharField(max_length=10, null=False, blank=False)
    complemento = models.CharField(max_length=45, null=False, blank=False)
    uf_cidade = models.CharField(max_length=25, null=False, blank=False)
    atendido = models.BooleanField(default=False)
    hora_cadastro = models.DateTimeField(auto_now_add=True)
    
    ativo = models.BooleanField(default=True)
    
class UsuarioModel(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nome} - {self.email}"
    
class PacienteForm(forms.ModelForm):
    class Meta:
        model = UsuarioModel
        fields = ['nome', 'email', 'senha']
