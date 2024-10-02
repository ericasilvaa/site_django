
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Article, ArticleHistory
from .forms import ArticleForm
from rest_framework import generics
from .serializers import ArticleSerializer
from rest_framework.permissions import IsAuthenticated

# Lista e criação de artigos
class ArticleListCreateView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]

# Detalhes, atualização e exclusão de um artigo específico
class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]

def article_list(request):
    sort_by = request.GET.get('sort', 'title')  # Ordena por título como padrão

    if sort_by == 'title':
        articles = Article.objects.all().order_by('title')
    elif sort_by == 'date':
        articles = Article.objects.all().order_by('-date')
    elif sort_by == 'authors':
        articles = Article.objects.all().order_by('authors')
    else:
        articles = Article.objects.all()  # Ordem padrão caso nada seja selecionado

    return render(request, 'app_project/article_list.html', {'articles': articles, 'sort_by': sort_by})
 

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'app_project/article_detail.html', {'article': article})

def article_create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
 
    else:
        form = ArticleForm()

    return render(request, 'app_project/article_form.html', {'form': form})

 
def article_update(request, pk):
    article = get_object_or_404(Article, pk=pk)

    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            # Salva as alterações no histórico antes de modificar
            ArticleHistory.objects.create(
                article=article,
                title=article.title,
                authors=article.authors,
                abstract=article.abstract,
                keywords=article.keywords
            )
            # Atualiza o artigo com os novos dados
            form.save()
            messages.success(request, 'Artigo atualizado com sucesso!')
            return redirect('article_detail', pk=article.pk)
    else:
 
        form = ArticleForm(instance=article)

    return render(request, 'app_project/article_form.html', {'form': form})

 
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        article.delete()
 
        return redirect('article_list')

    return render(request, 'app_project/article_delete.html', {'article': article})

def search_view(request):
    query = request.GET.get('q')
    if query: 
        results = Article.objects.filter(
            Q(title__icontains=query) |
            Q(authors__icontains=query) |
            Q(keywords__icontains=query)
        )
    else:
        results = Article.objects.none()

    return render(request, 'app_project/search_results.html', {'results': results, 'query': query}) 