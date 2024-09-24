from django.db import models
from django.core.validators import (
    RegexValidator, MinLengthValidator, MaxLengthValidator,
    MinValueValidator, MaxValueValidator, FileExtensionValidator
)
from rest_framework import serializers
import datetime


class Article(models.Model):
    title = models.CharField(max_length=200, validators=[MinLengthValidator(10)])
    authors = models.CharField(max_length=500)
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
    
    # Use a callable for dynamic year validation
    date = models.IntegerField(validators=[
        MinValueValidator(1900),
        MaxValueValidator(datetime.datetime.now().year)
    ])
    
    journal = models.CharField(max_length=200, blank=True, null=True)  # Optional field

    pdf_file = models.FileField(upload_to='articles/pdfs/', validators=[
        FileExtensionValidator(allowed_extensions=['pdf'])
    ])

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ArticleHistory(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='history')
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=500)
    abstract = models.TextField()
    keywords = models.CharField(max_length=400)
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