from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from datetime import datetime


from index.models import Paciente, ExameForm, Exame, PagamentoForm, AtendimentoForm, Atendimento

@login_required
def atendimento(request):
    if request.method == 'GET':
        pacientes_lista = Paciente.objects.all()
        return render(request, 'atendimento/atendimento.html', {'pacientes_em_atendimento': Paciente.objects.filter(data_cadastro=datetime.now()), 'pacientes_atendidos': Exame.objects.filter(data_exame=datetime.now()), 'pacientes_lista': pacientes_lista})

@login_required
def atendimento_cadastro(request):

    if request.method == 'POST':
        paciente_id = request.POST.get('id')
        paciente = Paciente.objects.get(guia=paciente_id)
        print(paciente)

        atendimento_form = AtendimentoForm(request.POST)
        pagamento_form = PagamentoForm(request.POST)

        if atendimento_form.is_valid() and pagamento_form.is_valid():
            atendimento = atendimento_form.save(commit=False)
            atendimento.id_paciente = paciente
            atendimento.save()

            pagamento = pagamento_form.save()  # Salvando o pagamento

            # Agora, atualize o atendimento com as IDs do exame e pagamento
            atendimento.id_pagamento_id = pagamento.id
            atendimento.save()

            return redirect('atendimento')
    else:
        atendimento_form = AtendimentoForm()
        pagamento_form = PagamentoForm()

    return render(request, 'atendimento/registrar.html', {
        'atendimento': atendimento_form,
        'pagamento': pagamento_form
    })


@login_required    
def atendimento_preenche_exame(request, id):
    
    paciente = Paciente.objects.get(id=id)
    
    if request.method == 'POST':    
        form = ExameForm(request.POST)
        atendimento = Atendimento()
        atendimento_id = Atendimento.objects.get(id_paciente=id, status=0)
        
        print(atendimento_id)
        
        if form.is_valid():            
            exame = form.save(commit=False)
            exame.paciente = paciente
            exame.save()
            
            atendimento.id_exame = paciente
            atendimento.save()
            
            return redirect('atendimento')
        
        else:
            print('erro')
            
        
    form = ExameForm()
    
    return render(request, 'atendimento-exame.html', {'form': form, 'paciente': paciente})

