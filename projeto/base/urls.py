"""
URL configuration for base project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from index.views import index_view, auth_login_view, auth_register_view, usuarios_view, atendimento_view, paciente_view


urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', index_view.index, name='index'),
    
    path('usuarios/', usuarios_view.UsuariosView.as_view(), name='usuarios'),
    
    path('auth_login/', auth_login_view.auth_login, name='auth_login'),
    path('auth_register/', auth_register_view.auth_register, name='auth_register'),
    path('auth_logout/', auth_login_view.auth_logout, name='auth_logout'),
    
    path('dashboard/', index_view.dashboard, name='dashboard'),
    path('profile/', index_view.profile, name='profile'),
    
    path('paciente/', paciente_view.paciente, name='paciente'),
    path('paciente/cadastro/', paciente_view.paciente_cadastro, name='paciente_cadastro'),
    path('paciente/editar/<int:id>/', paciente_view.paciente_editar, name='paciente_editar'),
    path('paciente/impressao/<int:id>/', paciente_view.paciente_ficha_impressao, name='paciente_ficha_impressao'),
    path('paciente/exames/lista/<int:id>/', paciente_view.paciente_exames_lista, name='paciente_exames_lista'),    
    
    path('atendimento/', atendimento_view.atendimento, name='atendimento'),
    path('atendimento/exame/<int:id>/', atendimento_view.atendimento_preenche_exame, name='atendimento_preencher_exame'),  
    
]
