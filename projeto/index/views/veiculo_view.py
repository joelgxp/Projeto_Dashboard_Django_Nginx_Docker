from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from ..models import Veiculo

@login_required
def get_veiculos(request):
    veiculos = Veiculo.objects.all()    
    return render(request, 'veiculo/veiculo.html', {'veiculos': veiculos})

@login_required
def get_veiculo(request, placa):
    veiculo = Veiculo.objects.get(placa=placa)
    return render(request, 'veiculo/veiculo.html', {'veiculo': veiculo})

@login_required
def create_veiculo(request):
    if request.method == 'GET':
        return render(request, 'veiculo/cadastro.html')
    
    Veiculo.objects.create(
        placa=request.POST.get('placa'),
        renavam=request.POST.get('renavam'),
        chassi=request.POST.get('chassi'),
        cor=request.POST.get('cor'),
        marca=request.POST.get('marca'),
        modelo=request.POST.get('modelo'),
        ano_fabricacao=request.POST.get('anoFabricacao'),
        ano_fabricacao_modelo=request.POST.get('anoModelo'),
        data_entrada=request.POST.get('dataEntrada'),
        complemento=request.POST.get('complemento'),
    )
    return render(request, 'veiculo/cadastro.html')