import uuid
import os

from django.db import models
from django import forms
from django.core.validators import validate_image_file_extension
from django.core.exceptions import ValidationError

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
    categoria = models.CharField(max_length=5, choices=CATEGORIA_CHOICES)
    solicitacao = models.CharField(max_length=25, choices=SOLICITACAO_CHOICES, null=False, blank=False)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_habilitacao = models.DateField(null=False, blank=False)
    nome_completo = models.CharField(max_length=200, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    sexo = models.CharField(max_length=25, choices=SEXO_CHOICES, null=False, blank=False)
    uf_emissor = models.CharField(max_length=2, null=False, blank=False)
    identidade = models.CharField(max_length=25, null=False, blank=False)
    orgao_emissor = models.CharField(max_length=25, null=False, blank=False)
    uf_naturalidade = models.CharField(max_length=2, null=False, blank=False)
    naturalidade = models.CharField(max_length=45, null=False, blank=False)
    
    nome_mae = models.CharField(max_length=200, null=False, blank=False)
    nome_pai = models.CharField(max_length=200, null=False, blank=False)
    logradouro = models.CharField(max_length=200, null=False, blank=False)
    numero = models.CharField(max_length=10, null=False, blank=False)
    bairro = models.CharField(max_length=45, null=False, blank=False)
    uf_cidade = models.CharField(max_length=2, null=False, blank=False)
    cidade = models.CharField(max_length=45, null=False, blank=False)
    cep = models.CharField(max_length=10, null=False, blank=False)
    complemento = models.CharField(max_length=45, null=False, blank=False)
    cpf = BRCPFField(max_length=14, null=False, blank=False)
    celular = models.CharField(max_length=15, null=False, blank=False)
    atendido = models.BooleanField(default=False)
    hora_cadastro = models.DateTimeField(auto_now_add=True)
    
    ativo = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.guia, self.registro, self.categoria, self.solicitacao, self.data_habilitacao, self.nome_completo, self.data_nascimento, self.sexo}"
    
class UsuarioModel(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nome} - {self.email}"
    
class PacienteForm(forms.ModelForm):
    class Meta:
        model = PacienteModel
        fields = ['guia', 
                  'registro', 
                  'categoria', 
                  'solicitacao',
                  'data_habilitacao',
                  'nome_completo',
                  'data_nascimento',
                  'sexo',
                  'uf_emissor',
                  'identidade',
                  'orgao_emissor',
                  'uf_naturalidade',
                  'naturalidade',
                  'nome_mae',
                  'nome_pai',
                  'logradouro',
                  'numero',
                  'bairro',
                  'uf_cidade',
                  'cidade',
                  'cep',
                  'complemento',
                  'cpf',
                  'celular'
                  ]
        
        widgets = {
            'guia': forms.NumberInput(attrs={'class': 'form-control', 'type': 'number'}),
            'registro': forms.NumberInput(attrs={'class': 'form-control', 'type': 'number'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'solicitacao': forms.Select(attrs={'class': 'form-select'}),
            'data_habilitacao': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            
            'identidade': forms.TextInput(attrs={'class': 'form-control'}),
            'orgao_emissor': forms.TextInput(attrs={'class': 'form-control'}),
            'naturalidade': forms.TextInput(attrs={'class': 'form-control'}),
            'nacionalidade': forms.TextInput(attrs={'class': 'form-select'}),
            
            'nome_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'sexo': forms.Select(attrs={'class': 'form-select'}),
            'uf_emissor': forms.TextInput(attrs={'class': 'form-control'}),
            'uf_naturalidade': forms.TextInput(attrs={'class': 'form-control'}),
            'nome_mae': forms.TextInput(attrs={'class': 'form-control'}),
            'nome_pai': forms.TextInput(attrs={'class': 'form-control'}),
            'logradouro': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control'}),
            'uf_cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'cep': forms.TextInput(attrs={'class': 'form-control'}),
            'complemento': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'celular': forms.TextInput(attrs={'class': 'form-control'}),
            
        }
        

    