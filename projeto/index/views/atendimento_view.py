from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from datetime import datetime


from index.models import Paciente, ExameForm, Exame, PagamentoForm, AtendimentoForm

@login_required
def atendimento(request):
    if request.method == 'GET':
        pacientes_lista = Paciente.objects.all()
        return render(request, 'atendimento.html', {'pacientes_em_atendimento': Exame.objects.filter(atendimento=1), 'pacientes_atendidos': Exame.objects.filter(data_exame=datetime.now()), 'pacientes_lista': pacientes_lista})
        
    elif request.method == 'POST':
        
        return render(request, 'atendimento.html')

        
@login_required
def atendimento_cadastro(request):
    paciente_lista = Paciente.objects.filter(data_cadastro=datetime.now())
    paciente = paciente_lista.first()

    if request.method == 'POST':
        atendimento_form = AtendimentoForm(request.POST)
        exame_form = ExameForm(request.POST)
        pagamento_form = PagamentoForm(request.POST)
        print(atendimento_form)
        if pagamento_form.is_valid():
            print('ok')
            atendimento_form.save()

            exame_form.save()

            pagamento_form.save()

            return redirect('atendimento')

    else:
        print('erro')
        atendimento_form = AtendimentoForm()
        exame_form = ExameForm()
        pagamento_form = PagamentoForm()

    return render(request, 'atendimento/registrar.html', {
        'paciente': paciente,
        'atendimento': atendimento_form,
        'exame': exame_form,
        'pagamento': pagamento_form
    })


@login_required    
def atendimento_preenche_exame(request, id):
    
    paciente = Paciente.objects.get(id=id)
    
    if request.method == 'POST':    
        form = ExameForm(request.POST)
        if form.is_valid():
            paciente.atendido = 0
            paciente.save()
            
            exame = form.save(commit=False)
            exame.paciente = paciente
            exame.save()
            return redirect('atendimento')
        
        else:
            print('erro')
            
        
    form = ExameForm()
    
    return render(request, 'atendimento-exame.html', {'form': form, 'paciente': paciente})

