from django.db import models

class auth_registerModel(models.Model):
    fullname = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome