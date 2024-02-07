from django.contrib import admin
from .models import Usuario, Paciente, PacienteExame

admin.site.register(Usuario)
admin.site.register(Paciente)
admin.site.register(PacienteExame)