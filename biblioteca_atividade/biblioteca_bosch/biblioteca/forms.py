from django import forms
from .models import Livro

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = '__all__' #pra não ter q pegar campo por campo
        # fields = ['nome', 'descricao'] 
