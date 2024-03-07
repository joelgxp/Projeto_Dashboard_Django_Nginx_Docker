from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime


from index.models import Paciente, ExameForm, Exame, PagamentoForm, AtendimentoForm, Atendimento

@login_required
def atendimento(request):
    if request.method == 'GET':
        pacientes_lista = Paciente.objects.all()
        return render(request, 'atendimento/atendimento.html', {
            'pacientes_em_atendimento': Atendimento.objects.filter(status=0), 
            'pacientes_atendidos': Atendimento.objects.filter(status=1), 
            'pacientes_lista': pacientes_lista})

@login_required
def atendimento_cadastro(request):

    if request.method == 'POST':
        paciente = request.POST.get('paciente')
        paciente_guia = Paciente.objects.get(guia=paciente)
        paciente_guia_id = paciente_guia.id
        
        atendimento_form = AtendimentoForm(request.POST)
        pagamento_form = PagamentoForm(request.POST)

        if Atendimento.objects.filter(guia=paciente).exists():
            erro = 'Paciente ja possui um atendimento em aberto!'
            return render(request, 'atendimento/registrar.html', {
                'erro': erro,
                'atendimento': atendimento_form,
                'pagamento': pagamento_form,
                'pacientes_por_data': Paciente.objects.filter(data_cadastro=datetime.now())
                })

        
        elif atendimento_form.is_valid() and pagamento_form.is_valid():
            atendimento = atendimento_form.save(commit=False)
            atendimento.id_paciente_id = paciente_guia_id
            atendimento.guia = paciente
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
        'pagamento': pagamento_form,
        'pacientes_por_data': Paciente.objects.filter(data_cadastro=datetime.now())
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
    
    return render(request, 'atendimento/exame-preencher.html', {'form': form, 'paciente': paciente})

