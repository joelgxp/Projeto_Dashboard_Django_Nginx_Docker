from django.db import models
from django import forms

class Veiculo(models.Model):
    placa = models.CharField(max_length=8)
    renavam = models.CharField(max_length=11)
    chassi = models.CharField(max_length=45)
    cor = models.CharField(max_length=25)
    marca = models.CharField(max_length=45)
    modelo = models.CharField(max_length=45)
    ano_fabricacao = models.IntegerField()
    ano_fabricacao_modelo = models.IntegerField()
    data_entrada = models.DateField()
    
    def __str__(self):
        return self.placa
    
class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = '__all__'