from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    nome = models.CharField(max_length=255)    
    ativo = models.BooleanField(default=True)
    
    REQUIRED_FIELDS = ['email', 'password']

    def __str__(self):
        return f"{self.username, self.email, self.password, self.last_login, self.is_superuser, self.is_staff, self.is_active, self.date_joined, self.ativo}"
    
class Veiculo(models.Model):
    placa = models.CharField(max_length=8)
    renavam = models.CharField(max_length=11)
    chassi = models.CharField(max_length=45, null=True, blank=True)
    cor = models.CharField(max_length=25)
    marca = models.CharField(max_length=45)
    modelo = models.CharField(max_length=45)
    ano_fabricacao = models.IntegerField()
    ano_fabricacao_modelo = models.IntegerField()
    data_entrada = models.DateField()
    complemento = models.CharField(max_length=250, null=True, blank=True)
    
    def __str__(self):
        return self.placa
    
class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = '__all__'