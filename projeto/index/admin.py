from django.contrib import admin
from .models import Usuario, Paciente, Exame

admin.site.register(Usuario)
admin.site.register(Paciente)
admin.site.register(Exame)