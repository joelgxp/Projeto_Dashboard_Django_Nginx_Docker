from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render


def auth_login(request):
    if request.method == 'GET':
        return render(request, 'auth-login.html', {
            'form' : AuthenticationForm
        })
        
    else:
        user = authenticate(request, email=request.POST.get('email'), password=request.POST.get('password'))

        if user is None:
            return render(request, '/auth_login', {
            'form' : AuthenticationForm,
            "error" : "Usuário ou senha inválido."                
            })
        else:
            login(request, user)
            return redirect('/index')
