from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('ver-livro/<int:id>/', views.ver_livro, name='ver-livro'),
    path('cadastrar-livro/', views.cadastrar_livro, name='cadastrar-livro'),
    path('excluir-livro/<int:id>/', views.excluir_livro, name='excluir-livro'),
    path('cadastrar-categoria/', views.cadastrar_categoria, name='cadastrar-categoria'),
    path('cadastrar-emprestimo/', views.cadastrar_emprestimo, name='cadastrar-emprestimo'),
    path('devolver-livro/', views.devolver_livro, name='devolver-livro'),
    path('alterar-livro', views.alterar_livro, name='alterar-livro'),
]