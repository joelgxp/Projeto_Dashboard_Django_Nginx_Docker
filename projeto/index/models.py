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
    SEXO_CHOICES = (
        ('MASCULINO', "MASCULINO"),
        ('FEMININO', "FEMININO")
    )  
    guia = models.IntegerField(null=False, blank=False, unique=True)
    registro = models.CharField(max_length=9, null=False, blank=False)
    categoria = models.CharField(max_length=5, choices=CATEGORIA_CHOICES)
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

    hora_cadastro = models.DateTimeField(auto_now_add=True)
    
    ativo = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.guia, self.registro, self.categoria, self.data_habilitacao, self.nome_completo, self.data_nascimento, self.sexo}"
 
class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['guia', 
                  'registro', 
                  'categoria', 
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
                  'celular'
                  ]
        
        widgets = {
            'guia': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'registro': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
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
            
        }
        
class Exame(models.Model):
    CHOICES_CONCLUSAO = (
        ('apto', 'APTO'),
        ('inapto', 'INAPTO'),
    )
    CHOICE_CORRECAO_VISUAL = (
        ('sim', 'SIM'),
        ('nao', 'NÃO'),
    )  
    data_exame = models.DateField(null=True, blank=True)
    visao_le = models.IntegerField(null=True, blank=True)
    visao_ld = models.IntegerField(null=True, blank=True)
    correcao_visual = models.CharField(choices=CHOICE_CORRECAO_VISUAL, max_length=10, null=True, blank=True)
    campo_visual_le = models.IntegerField(null=True, blank=True)
    campo_visual_ld = models.IntegerField(null=True, blank=True)
    exame_validade = models.DateField(null=True, blank=True)
    conclusao = models.CharField(choices=CHOICES_CONCLUSAO, max_length=10, null=True, blank=True)
    complemento = models.CharField(max_length=255, null=True, blank=True)
    
class ExameForm(forms.ModelForm):
    class Meta:
        model = Exame
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
        
class Pagamento(models.Model):
    CHOICES_METODO_PAGAMENTO = (
        ('PIX', "PIX"),
        ('DINHEIRO', "DINHEIRO"),
        ('PIX/DINHEIRO', "PIX/DINHEIRO"),
    )
    data = models.DateField(auto_now_add=True)
    valor_pix = models.FloatField(null=False, blank=False, default=0)
    valor_dinheiro = models.FloatField(null=False, blank=False, default=0)
    valor_total = models.FloatField(null=True, blank=True)
    metodo_pagamento = models.CharField(choices=CHOICES_METODO_PAGAMENTO, max_length=45)
    
class PagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields = ['valor_pix', 'valor_dinheiro', 'valor_total', 'metodo_pagamento']
        widgets = {
            'valor_pix': forms.TextInput(attrs={'class': 'form-control'}),
            'valor_dinheiro': forms.TextInput(attrs={'class': 'form-control'}),
            'valor_total': forms.TextInput(attrs={'class': 'form-control'}),
            'metodo_pagamento': forms.Select(attrs={'class': 'form-select'}),
        }
        
class Atendimento(models.Model):
    CHOICE_SOLICITACAO = (
        ('PRIMEIRA_HABILITACAO', "PRIMEIRA HABILITAÇÃO"),
        ('RENOVACAO', "RENOVAÇÃO"),
        ('RENOVACAO_ATIV_REM', "RENOVAÇÃO ATIV. REMUNERADA"),
        ('ADICAO_CATEGORIA', "ADIÇÃO DE CATEGORIA"),
        ('MUDANCA_CATEGORIA', "MUDANÇA DE CATEGORIA"),
        ('ALTERACAO_DADOS', "ALTERAÇÃO DE DADOS")
    )
    guia = models.IntegerField(null=False, blank=False, unique=True)
    solicitacao = models.CharField(max_length=45, choices=CHOICE_SOLICITACAO, null=False, blank=False)
    data = models.DateField(null=False, blank=False, auto_now_add=True)
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=True, blank=True)
    id_exame = models.ForeignKey(Exame, on_delete=models.CASCADE, null=True, blank=True)
    id_pagamento = models.ForeignKey(Pagamento, on_delete=models.CASCADE, null=True, blank=True)
    status = models.BooleanField(default=False)
    
class AtendimentoForm(forms.ModelForm):
    class Meta:
        model = Atendimento
        fields = ['solicitacao', 'id_paciente', 'id_exame', 'id_pagamento', 'status']
        widgets = {
            'solicitacao': forms.Select(attrs={'class': 'form-select'}),    
            'id_paciente': forms.Select(attrs={'class': 'form-select'}),
            'id_exame': forms.Select(attrs={'class': 'form-select'}),
            'id_pagamento': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }