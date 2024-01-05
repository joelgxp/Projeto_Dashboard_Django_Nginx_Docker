from django.shortcuts import render, redirect
from index.models.lider_model import LiderForm, LiderModel

def lider(request):
    lideres = LiderModel.objects.all()
    return render(request, 'lider.html', {'lideres': lideres})

def criar_lider(request):
    
    if request.method == 'POST': 
        form = LiderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/lider')             

    else:
        return render(request, 'lider.html', {
            'form': form,
        })
            
