from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from index.models import Paciente, PacienteForm, Exame

@login_required
def paciente(request):
    if request.method == 'GET':
        pacientes = Paciente.objects.all()
        form = PacienteForm()
        return render(request, 'paciente.html', {'pacientes': pacientes, 'form': form})

@login_required
def paciente_cadastro(request):
    
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('paciente'))
        else:
            
            print('erro')
    else:
        form = PacienteForm()
            
    return render(request, 'paciente-cadastro.html', {'form': form})       
        
@login_required
def paciente_editar(request, id):    
    paciente = Paciente.objects.get(id=id)
    
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('paciente'))
        else:            
            print('erro')
    else:
        form = PacienteForm(instance=paciente)
    return render(request, 'paciente-editar.html', {'form': form, 'paciente': paciente})

@login_required      
def paciente_ficha_impressao(request, id):    
    paciente = Paciente.objects.get(id=id)
              
    return render(request, 'paciente-ficha-impressao.html', {'paciente': paciente})

@login_required
def paciente_exames_lista(request, id):
    exame = Exame.objects.filter(paciente=id)
    
    return render(request, 'atendimento-exames-lista.html', {'exames': exame})

