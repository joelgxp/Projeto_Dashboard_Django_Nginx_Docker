from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from datetime import datetime


from index.models import Paciente, PacienteExameForm, PacienteExame

@login_required
def atendimento(request):
    if request.method == 'GET':
        pacientes_lista = Paciente.objects.all()
        return render(request, 'atendimento.html', {'pacientes_em_atendimento': Paciente.objects.filter(atendido=1), 'pacientes_atendidos': PacienteExame.objects.filter(data_exame=datetime.now()), 'pacientes_lista': pacientes_lista})
        
    elif request.method == 'POST':
        
        return render(request, 'atendimento.html')

@login_required    
def atendimento_preenche_exame(request, id):
    
    paciente = Paciente.objects.get(id=id)
    
    if request.method == 'POST':    
        form = PacienteExameForm(request.POST)
        if form.is_valid():
            paciente.atendido = 0
            paciente.save()
            
            exame = form.save(commit=False)
            exame.paciente = paciente
            exame.save()
            return redirect('atendimento')
        
    else:
        form = PacienteExameForm()
        print('erro')
    
    return render(request, 'atendimento-exame.html', {'form': form, 'paciente': paciente})

