from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from index.models import PacienteModel, PacienteForm
def paciente(request):
    if request.method == 'GET':
        pacientes = PacienteModel.objects.all()
        form = PacienteForm()
        return render(request, 'paciente.html', {'pacientes': pacientes, 'form': form})

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

def paciente_encaminha_atendimento(id):
    paciente = PacienteModel.objects.get(id=id)
    paciente.atendido = True
    paciente.save()
    
    return HttpResponseRedirect(reverse('atendimento'))
    


# def criar_paciente(request):
    
#     if request.method == 'POST': 
#         guia = request.POST.get('guia')
#         registro = request.POST.get('registro')
#         categoria = request.POST.get('categoria')
#         solicitacao = request.POST.get('solicitacao')
#         data_habilitacao = request.POST.get('data_habilitacao')
#         nome_completo = request.POST.get('nome_completo')
#         data_nascimento = request.POST.get('data_nascimento')
#         sexo = request.POST.get('sexo')
#         identidade = request.POST.get('identidade')
#         orgao_emissor = request.POST.get('orgao_emissor')
#         uf_emissor = request.POST.get('uf_emissor')
#         naturalidade = request.POST.get('naturalidade')
#         uf_naturalidade = request.POST.get('uf_naturalidade')
#         nome_mae = request.POST.get('nome_mae')
#         nome_pai = request.POST.get('nome_pai')
#         celular = request.POST.get('celular')
#         cpf = request.POST.get('cpf')
#         logradouro = request.POST.get('logradouro')
#         numero = request.POST.get('numero')
#         bairro = request.POST.get('bairro')
#         cidade = request.POST.get('cidade')
#         cep = request.POST.get('cep')
#         complemento = request.POST.get('complemento')
#         uf_cidade = request.POST.get('uf_cidade')              
        
#         try:
#             paciente = PacienteModel.objects.create(
#                 guia = guia,
#                 registro = registro,
#                 categoria = categoria,
#                 solicitacao = solicitacao,
#                 data_habilitacao = data_habilitacao,
#                 nome_completo = nome_completo,
#                 data_nascimento = data_nascimento,
#                 sexo = sexo,
#                 identidade = identidade,
#                 orgao_emissor = orgao_emissor,
#                 uf_emissor = uf_emissor,
#                 naturalidade = naturalidade,
#                 uf_naturalidade = uf_naturalidade,
#                 nome_mae = nome_mae,
#                 nome_pai = nome_pai,
#                 celular = celular,
#                 cpf = cpf,
#                 logradouro = logradouro,
#                 numero = numero,
#                 bairro = bairro,
#                 cidade = cidade,
#                 cep = cep,
#                 complemento = complemento,
#                 uf_cidade = uf_cidade,
#                 ativo = True                
#             )
#             paciente.save()
            
#             return HttpResponse('Paciente Cadastrado com Sucesso', status=200)
            
#         except Exception as e:
#             return HttpResponse('Erro ao Cadastrar Paciente'+ str(e), status=500)
        
#     return render(request, 'paciente.html', {'form': PacienteForm})
    
            
