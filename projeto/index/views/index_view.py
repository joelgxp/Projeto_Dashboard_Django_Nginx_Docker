from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime

from index.models import Paciente, Exame

@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def dashboard(request):
    pacientes_em_atendimento = Paciente.objects.filter()
    pacientes_atendidos = Exame.objects.filter(data_exame=datetime.now())
    return render(request, 'dashboard.html', {'pacientes_em_atendimento': pacientes_em_atendimento, 
                                              'pacientes_atendidos': pacientes_atendidos, 
                                              'pacientes_lista': Paciente.objects.all()})

@login_required
def profile(request):
    return render(request, 'profile.html')