from django import forms
from .models import Article
from django.core.exceptions import ValidationError

class ArticleForm(forms.ModelForm):
    date = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Ano (ex: 2000)'}),
        label='Data'
    )

    class Meta:
        model = Article
        fields = ['title', 'authors', 'abstract', 'keywords', 'date', 'journal', 'pdf_file']
        labels = {
            'title': 'Título',
            'authors': 'Autores',
            'abstract': 'Resumo',
            'keywords': 'Palavras-chave',
            'date': 'Data',
            'journal': 'Jornal',
            'pdf_file': 'Arquivo PDF',
        }