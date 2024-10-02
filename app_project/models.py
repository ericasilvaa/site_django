from django.db import models
<<<<<<< HEAD
from django.core.validators import RegexValidator
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import FileExtensionValidator
import datetime

class Article(models.Model):
    title = models.CharField(max_length=200, validators=[MinLengthValidator(10)])
    authors = models.CharField(max_length=500 #,  validators=[
    #RegexValidator(
    #    regex=r'^[A-Za-zÀ-ÖØ-öø-ÿ,;\s]+$',
    #    message='Use um formato válido: "Sobrenome, Nome; Sobrenome, Nome".'
    #)
)
=======
from django.core.validators import (
    RegexValidator, MinLengthValidator, MaxLengthValidator,
    MinValueValidator, MaxValueValidator, FileExtensionValidator
)
from rest_framework import serializers
import datetime


class Article(models.Model):
    title = models.CharField(max_length=200, validators=[MinLengthValidator(10)])
    authors = models.CharField(max_length=500)
>>>>>>> parte2/main
    abstract = models.TextField(validators=[
        MinLengthValidator(100),
        MaxLengthValidator(1500)
    ])
    keywords = models.CharField(max_length=400, validators=[
        RegexValidator(
            regex=r'^[A-Za-zÀ-ÖØ-öø-ÿ\s]+(\.\s*[A-Za-zÀ-ÖØ-öø-ÿ\s]+)*\.$',
            message='As palavras-chave devem ser frases separadas por ponto e espaço (ex: "Frase 1. Frase 2.").'
        )
    ])
<<<<<<< HEAD
=======
    
    # Use a callable for dynamic year validation
>>>>>>> parte2/main
    date = models.IntegerField(validators=[
        MinValueValidator(1900),
        MaxValueValidator(datetime.datetime.now().year)
    ])
<<<<<<< HEAD
    journal = models.CharField(max_length=200)
    pdf_file = models.FileField(upload_to='http://127.0.0.1:8000/article/7/', validators=[
        FileExtensionValidator(allowed_extensions=['pdf'])])
=======
    
    journal = models.CharField(max_length=200, blank=True, null=True)  # Optional field

    pdf_file = models.FileField(upload_to='articles/pdfs/', validators=[
        FileExtensionValidator(allowed_extensions=['pdf'])
    ])
>>>>>>> parte2/main

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

<<<<<<< HEAD
=======

>>>>>>> parte2/main
class ArticleHistory(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='history')
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=500)
    abstract = models.TextField()
    keywords = models.CharField(max_length=400)
<<<<<<< HEAD
    updated_at = models.DateTimeField(auto_now_add=True)  # Quando essa versão foi criada

    def __str__(self):
        return f"Versão de {self.updated_at.strftime('%d/%m/%Y %H:%M')} do artigo '{self.article.title}'"
=======
    updated_at = models.DateTimeField(auto_now_add=True)  # Version creation timestamp

    def __str__(self):
        return f"Version from {self.updated_at.strftime('%d/%m/%Y %H:%M')} of article '{self.article.title}'"


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'id', 'title', 'authors', 'abstract', 
            'keywords', 'date', 'journal', 'pdf_file', 
            'created_at', 'updated_at'
        ]

    def validate_date(self, value):
        """Ensure the date is not in the future."""
        if value > datetime.datetime.now().year:
            raise serializers.ValidationError("The date cannot be in the future.")
        return value
>>>>>>> parte2/main
