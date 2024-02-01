from django.shortcuts import render

def atendimento(request):
    return render(request, 'fila-atendimento.html')