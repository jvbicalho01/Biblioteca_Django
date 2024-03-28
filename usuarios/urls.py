from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('valida-cadastro/', views.valida_cadastro, name='valida-cadastro'),
    path('valida-login/', views.valida_login, name='valida-login'),
    path('sair/', views.sair, name='sair'),
]