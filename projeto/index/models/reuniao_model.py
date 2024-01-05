from django import forms
from django.db import models

class ReuniaoModel(models.Model):
    data = models.DateField()
    
    def __str__(self):
        return f"{self.data}"
    
class ReuniaoForm(forms.ModelForm):
    class Meta:
        model = ReuniaoModel
        fields = ['data']
