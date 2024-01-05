from django import forms
from django.db import models

class auth_registerModel(models.Model):
    fullname = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
    
class auth_registerForm(forms.ModelForm):
    class Meta:
        model = auth_registerModel
        fields = ['nome', 'email', 'password']