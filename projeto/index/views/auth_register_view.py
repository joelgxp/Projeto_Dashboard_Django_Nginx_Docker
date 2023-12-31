from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

def auth_register(request):
    
    if request.method == 'GET':
        return render(request, 'auth-register.html', {
            'form' : UserCreationForm
        })
        
    else:
    
        if request.POST['password'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['fullname'], email=request.POST['email'], password=request.POST['password'])
                user.save()
                login(request, user)
                return redirect('/auth_login')
            except:
                return render(request, 'auth-register.html', {
                'form' : UserCreationForm,
                "error" : "Usuário ja cadastrado."                
                })
                
    return render(request, '/auth_register', {
        'form' : UserCreationForm,
        "error" : "Senhas diferentes."
    })

