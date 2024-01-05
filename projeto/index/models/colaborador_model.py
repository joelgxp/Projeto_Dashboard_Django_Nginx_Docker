from django.db import models
from django import forms

class colaboradorModel(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    senha = models.CharField(max_length=255)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nome} - {self.email} - {self.departamento}"
     
class colaboradorForm(forms.ModelForm):
    class Meta:
        model = colaboradorModel
        fields = ['nome', 'departamento', 'email', 'senha']
