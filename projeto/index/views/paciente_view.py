from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

from index.models import Paciente, PacienteForm

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

def paciente_encaminha_atend(id):
    try:
        # Verifica se o paciente existe no banco de dados
        paciente = Paciente.objects.get(id=id)
        print(paciente)
    except ObjectDoesNotExist:
        # Tratar o caso em que o paciente não existe
        print(f"Paciente com ID {id} não encontrado.")
        return

    # Atualiza o estado do paciente para atendido
    Paciente.objects.filter(id=id).update(atendido=True)
        
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
        
def paciente_ficha_impressao(request, id):    
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
            
    return render(request, 'paciente-ficha-impressao.html', {'form': form, 'paciente': paciente})
