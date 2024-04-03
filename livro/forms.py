from django.db import models
from datetime import date
from django import forms

from .models import Categoria, Livros

class CadastroLivro(forms.ModelForm):
    class Meta:
        model = Livros
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['usuario'].widget = forms.HiddenInput()
