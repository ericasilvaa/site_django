from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import FileExtensionValidator
import datetime

class Article(models.Model):
    title = models.CharField(max_length=200, validators=[MinLengthValidator(10)])
    authors = models.CharField(max_length=500,  validators=[
    RegexValidator(
        regex=r'^[A-Za-zÀ-ÖØ-öø-ÿ,;\s]+$',
        message='Use um formato válido: "Sobrenome, Nome; Sobrenome, Nome".'
    )
])
    abstract = models.TextField(validators=[
        MinLengthValidator(100),
        MaxLengthValidator(1000)
    ])
    keywords = models.CharField(max_length=255, validators=[
    RegexValidator(
        regex=r'^[A-Za-zÀ-ÖØ-öø-ÿ,\s]+$',
        message='As palavras-chave devem ser separadas por vírgulas.'
    )
])
    date = models.IntegerField(validators=[
        MinValueValidator(1900),
        MaxValueValidator(datetime.datetime.now().year)
    ])
    journal = models.CharField(max_length=200)
    pdf_file = models.FileField(upload_to='http://127.0.0.1:8000/article/7/', validators=[
        FileExtensionValidator(allowed_extensions=['pdf'])])

    
    def __str__(self):
        return self.title
