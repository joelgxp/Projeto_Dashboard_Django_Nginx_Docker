from django.shortcuts import redirect, render
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from index.models import Usuario

@login_required
def auth_register(request):    
    if request.method == 'GET':
        return render(request, 'auth-register.html')
        
    else:
        username =  request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password2')
    
        if password == password_confirm:
            
            if Usuario.objects.filter(email=email).exists():                
                print("usuario ja existe")
                return redirect('auth_register')
                           
            try:
                Usuario.objects.create_user(username=username, email=email, password=password)
                print("entrou aqui2")
                return redirect('auth_login')
            except Exception as e:
                print("Erro ao criar: ", e)
                return redirect('auth_register')
                
        else:
            messages.add_message(request, constants.ERROR, 'As senhas não coincídem.')
            return render(request, 'auth-register.html')


