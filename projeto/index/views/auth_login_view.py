from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.messages import constants
from django.contrib import messages


def auth_login(request):
    if request.method == 'GET':
        return render(request, 'auth-login.html')
        
    elif request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username, password)     
        user = authenticate(request, username=username, password=password)
        
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.add_message(request, constants.ERROR, 'Usuario ou senha inválidos.')
            return redirect('auth_login')

@login_required        
def auth_logout(request):
    return render(request, 'auth-logout.html')
        