from django.db import models

# Create your models here.
# Teste

class Article(models.Model):
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=500)
    abstract = models.TextField()
    keywords = models.CharField(max_length=500)
    date = models.PositiveIntegerField()
    journal = models.CharField(max_length=200)
    pdf_file = models.FileField(upload_to='pdfs/')
    
    def __str__(self):
        return self.title
