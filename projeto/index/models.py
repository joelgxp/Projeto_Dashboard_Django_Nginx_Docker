from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser

from localflavor.br.models import BRCPFField
    
class Usuario(AbstractUser):
    nome = models.CharField(max_length=255)    
    ativo = models.BooleanField(default=True)
    
    REQUIRED_FIELDS = ['email', 'password']

    def __str__(self):
        return f"{self.username, self.email, self.password, self.last_login, self.is_superuser, self.is_staff, self.is_active, self.date_joined, self.ativo}"
   
class Paciente(models.Model):
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
        ('PRIMEIRA_HABILITACAO', "PRIMEIRA HABILITAÇÃO"),
        ('RENOVACAO', "RENOVAÇÃO"),
        ('RENOVACAO_ATIV_REM', "RENOVAÇÃO ATIV. REMUNERADA"),
        ('ADICAO_CATEGORIA', "ADIÇÃO DE CATEGORIA"),
        ('MUDANCA_CATEGORIA', "MUDANÇA DE CATEGORIA"),
        ('ALTERACAO_DADOS', "ALTERAÇÃO DE DADOS")
    )
    SEXO_CHOICES = (
        ('MASCULINO', "MASCULINO"),
        ('FEMININO', "FEMININO")
    )
    ENCAMINHA_EXAME_CHOICES = (
        ('1', "SIM"),
        ('2', "NÃO")
    )
    
    guia = models.IntegerField(null=False, blank=False)
    registro = models.CharField(max_length=9, null=False, blank=False)
    categoria = models.CharField(max_length=5, choices=CATEGORIA_CHOICES)
    solicitacao = models.CharField(max_length=45, choices=SOLICITACAO_CHOICES, null=False, blank=False)
    data_cadastro = models.DateField(null=False, blank=False)
    data_habilitacao = models.DateField(null=False, blank=False)
    nome_completo = models.CharField(max_length=80, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    sexo = models.CharField(max_length=25, choices=SEXO_CHOICES, null=False, blank=False)
    uf_emissor = models.CharField(max_length=2, null=False, blank=False)
    identidade = models.CharField(max_length=25, null=False, blank=False)
    orgao_emissor = models.CharField(max_length=25, null=False, blank=False)
    uf_naturalidade = models.CharField(max_length=2, null=False, blank=False)
    naturalidade = models.CharField(max_length=45, null=False, blank=False)
    
    nome_mae = models.CharField(max_length=80, null=False, blank=False)
    nome_pai = models.CharField(max_length=80, null=False, blank=False)
    logradouro = models.CharField(max_length=80, null=False, blank=False)
    numero = models.CharField(max_length=10, null=False, blank=False)
    bairro = models.CharField(max_length=45, null=False, blank=False)
    uf_cidade = models.CharField(max_length=2, null=False, blank=False)
    cidade = models.CharField(max_length=45, null=False, blank=False)
    cep = models.CharField(max_length=10, null=False, blank=False)
    complemento = models.CharField(max_length=45, null=False, blank=False)
    cpf = BRCPFField(max_length=14, null=False, blank=False)
    celular = models.CharField(max_length=15, null=False, blank=False)
    atendido = models.CharField(max_length=5, choices=ENCAMINHA_EXAME_CHOICES, null=False, blank=False)

    hora_cadastro = models.DateTimeField(auto_now_add=True)
    
    ativo = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.guia, self.registro, self.categoria, self.solicitacao, self.data_habilitacao, self.nome_completo, self.data_nascimento, self.sexo, self.atendido}"
 
class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['guia', 
                  'registro', 
                  'categoria', 
                  'solicitacao',
                  'data_cadastro',
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
                  'celular',
                  'atendido'
                  ]
        
        widgets = {
            'guia': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'registro': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'solicitacao': forms.Select(attrs={'class': 'form-select'}),
            'data_cadastro': forms.DateInput(attrs={'class': 'form-control'}),
            'data_habilitacao': forms.DateInput(attrs={'class': 'form-control'}),
            
            'identidade': forms.TextInput(attrs={'class': 'form-control'}),
            'orgao_emissor': forms.TextInput(attrs={'class': 'form-control'}),
            'naturalidade': forms.TextInput(attrs={'class': 'form-control'}),
            'nacionalidade': forms.TextInput(attrs={'class': 'form-select'}),
            
            'nome_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control'}),
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
            
            'atendido': forms.Select(attrs={'class': 'form-select'}),
            
        }
        
class PacienteExame(models.Model):
    CHOICES_CONCLUSAO = (
        ('apto', 'Apto'),
        ('inapto', 'Inapto'),
    )
    CHOICE_CORRECAO_VISUAL = (
        ('sim', 'Sim'),
        ('nao', 'Não'),
    )
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)    
    data_exame = models.DateField()
    visao_le = models.IntegerField()
    visao_ld = models.IntegerField()
    correcao_visual = models.CharField(choices=CHOICE_CORRECAO_VISUAL, max_length=10)
    campo_visual_le = models.IntegerField()
    campo_visual_ld = models.IntegerField()
    exame_validade = models.DateField()
    conclusao = models.CharField(choices=CHOICES_CONCLUSAO, max_length=10)
    complemento = models.CharField(max_length=255, null=True, blank=True)
    
class PacienteExameForm(forms.ModelForm):
    class Meta:
        model = PacienteExame
        fields = ['data_exame', 'visao_le', 'visao_ld', 'correcao_visual', 'campo_visual_le', 'campo_visual_ld', 'exame_validade', 'conclusao', 'complemento']
        widgets = {
            'data_exame': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'visao_le': forms.TextInput(attrs={'class': 'form-control'}),
            'visao_ld': forms.TextInput(attrs={'class': 'form-control'}),
            'correcao_visual': forms.Select(attrs={'class': 'form-select'}),
            'campo_visual_le': forms.TextInput(attrs={'class': 'form-control'}),
            'campo_visual_ld': forms.TextInput(attrs={'class': 'form-control'}),
            'exame_validade': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'conclusao': forms.Select(attrs={'class': 'form-select'}),
            'complemento': forms.TextInput(attrs={'class': 'form-control'}),
            
        }
        
class FluxoDeCaixa(models.Model):
    CHOICES_METODO_PAGAMENTO = (
        ('PIX', "PIX"),
        ('DINHEIRO', "DINHEIRO"),
        ('PIX/DINHEIRO', "PIX/DINHEIRO"),
    )
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)
    valor_pix = models.FloatField(null=False, blank=False)
    valor_dinheiro = models.FloatField(null=False, blank=False)
    valor_total = models.FloatField(null=True, blank=True)
    metodo_pagamento = models.CharField(choices=CHOICES_METODO_PAGAMENTO, max_length=45)
    
class FluxoDeCaixaForm(forms.ModelForm):
    class Meta:
        model = FluxoDeCaixa
        fields = ['valor_pix', 'valor_dinheiro', 'valor_total', 'metodo_pagamento']
        widgets = {
            'valor_pix': forms.TextInput(attrs={'class': 'form-control'}),
            'valor_dinheiro': forms.TextInput(attrs={'class': 'form-control'}),
            'valor_total': forms.TextInput(attrs={'class': 'form-control'}),
            'metodo_pagamento': forms.Select(attrs={'class': 'form-select'}),
        }