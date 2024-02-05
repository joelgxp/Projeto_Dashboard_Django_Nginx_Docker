from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from index.models import Paciente

@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def dashboard(request):
    pacientes_em_atendimento = Paciente.objects.filter(atendido=True)
    return render(request, 'dashboard.html', {'pacientes_em_atendimento': pacientes_em_atendimento, 'pacientes_lista': Paciente.objects.all()})

@login_required
def profile(request):
    return render(request, 'profile.html')