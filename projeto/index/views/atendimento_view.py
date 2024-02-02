from django.shortcuts import render

from index.models import PacienteModel, PacienteExameForm

def atendimento(request):
    if request.method == 'GET':
        pacientes_lista = PacienteModel.objects.all()
        if pacientes_lista.filter(atendido=True):
            pacientes = PacienteModel.objects.filter(atendido=True)
            return render(request, 'atendimento.html', {'pacientes_em_atendimento': pacientes})
        else:
            pacientes = PacienteModel.objects.filter(atendido=False)
            return render(request, 'atendimento.html', {'pacientes_atendidos': pacientes})
    elif request.method == 'POST':
        
        return render(request, 'atendimento.html')
    
def atendimento_preenche_exame(request, id):
    
    paciente = PacienteModel.objects.get(id=id)
    paciente_id = paciente.id
    
    if request.method == 'POST':    
        form = PacienteExameForm(request.POST)
        if form.is_valid():
            exame = form.save(commit=False)
            exame.paciente = paciente_id
            exame.save()
        
    else:
        form = PacienteExameForm()
        print('erro')
    
    return render(request, 'atendimento-exame.html', {'form': form, 'paciente': paciente})