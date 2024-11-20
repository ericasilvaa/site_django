from rest_framework import serializers
from .models import Article
<<<<<<< HEAD
=======
import datetime

>>>>>>> Parte 3

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
<<<<<<< HEAD
        fields = '__all__'  # Isso deve incluir todos os campos do modelo
=======
        fields = [
            'id', 'title', 'authors', 'abstract',
            'keywords', 'date', 'journal', 'pdf_file',
            'created_at', 'updated_at', 'created_by', 'updated_by'
        ]

    def validate_date(self, value):
        """Garantir que a data não está no futuro."""
        if value > datetime.datetime.now().year:
            raise serializers.ValidationError("A data não pode estar no futuro.")
        return value
>>>>>>> Parte 3
