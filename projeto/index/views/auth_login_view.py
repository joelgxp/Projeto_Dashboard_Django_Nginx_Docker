from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


def auth_login(request):
    if request.method == 'GET':
        return render(request, 'auth-login.html', {
            'form' : AuthenticationForm
        })
        
    else:
        
        user = authenticate(
            request, email=request.POST['email'], password=request.POST['password'])

        if user is None:
            return render(request, 'auth-login.html', {
                'form' : AuthenticationForm,
                "error" : "Usuário ou senha inválido."                
            })
        else:
            login(request, user)
            return redirect('/index')
        
def auth_logout(request):
    return render(request, 'auth-logout.html')
        