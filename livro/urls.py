from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('ver-livro/<int:id>/', views.ver_livro, name='ver-livro'),
    path('cadastrar-livro', views.cadastrar_livro, name='cadastrar-livro'),
]