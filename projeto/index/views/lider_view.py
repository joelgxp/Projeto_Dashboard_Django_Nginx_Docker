from django.shortcuts import render, redirect
from index.models import PacienteModel, PacienteForm
def paciente(request):
    pacientes = PacienteModel.objects.all()
    return render(request, 'paciente.html', {'pacientes': pacientes})

def criar_lider(request):
    
    if request.method == 'POST': 
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/paciente')             

    else:
        return render(request, 'paciente.html', {
            'form': form,
        })
            
