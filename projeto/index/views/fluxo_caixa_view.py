from django.shortcuts import render
from django.shortcuts import redirect

from ..models import Pagamento, PagamentoForm, Paciente, Exame

def fluxo_caixa(request):
    # Recupera todos os pagamentos
    tipo_solicitacao = Paciente.objects.all()
    print(tipo_solicitacao)
    pagamentos = Pagamento.objects.all()

    # Inicializa a soma dos valores de dinheiro e pix
    total_dinheiro = 0
    total_pix = 0

    # Itera sobre cada objeto do QuerySet para somar os valores
    for pagamento in pagamentos:
        total_dinheiro += pagamento.valor_dinheiro
        total_pix += pagamento.valor_pix

    # Soma total
    total = total_dinheiro + total_pix

    print('Total Dinheiro:', total_dinheiro)
    print('Total PIX:', total_pix)
    print('Total:', total)

    return render(request, 'fluxo-caixa/fluxo-caixa.html', {
        'pagamentos': pagamentos,
        'total_dinheiro': total_dinheiro,
        'total_pix': total_pix,
        'total': total
    })
    
def fluxo_caixa_pagamento(request, id):
    
    paciente = Paciente.objects.get(id=id)
    pacienteexame = Exame.objects.get(id=id)
        
    if request.method == 'POST':
        form = PagamentoForm(request.POST)
        print(form)
        if form.is_valid():
            pagamento = form.save(commit=False)
            pagamento.paciente = paciente
            soma = form.cleaned_data['valor_dinheiro'] + form.cleaned_data['valor_pix']
            pagamento.valor_total = soma
            pagamento.save()
            return redirect('fluxo_caixa')
            
        else:
            print('erro')
            
    pagamento = PagamentoForm()        
    
    return render(request, 'fluxo-caixa/fluxo-caixa-pagamento.html', {'paciente': paciente, 'pagamento': pagamento, 'pacienteexame': pacienteexame})