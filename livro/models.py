from django.db import models

class Livros(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=30)
    co_autor = models.CharField(max_length=30)
    data_cadastro = models.DateField()
    emprestado = models.BooleanField(default=False)
    nome_emprestado = models.CharField(max_length=30)
    data_emprestimo = models.DateTimeField()
    data_devolução = models.DateTimeField()
    tempo_duracao = models.DateField()