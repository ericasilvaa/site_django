#from django.shortcuts import render
#def home (request):
#    return render(request,'usuarios/home.html')

from django.shortcuts import render, get_object_or_404, redirect
from django.template import TemplateDoesNotExist
from .models import Article, ArticleHistory
from .forms import ArticleForm
from django.contrib import messages
from django.db.models import Q
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'app_project/article_list.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'app_project/article_detail.html', {'article': article})

def article_create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Artigo cadastrado com sucesso!')  # Mensagem de sucesso
            return redirect('article_list')
        else:
            messages.error(request, 'Erro ao cadastrar o artigo. Verifique os dados informados.')  # Mensagem de erro
    else:
        form = ArticleForm()

    return render(request, 'app_project/article_form.html', {'form': form})


def article_update(request, pk):
    # Recupera o artigo que você deseja editar
    article = get_object_or_404(Article, pk=pk)

    if request.method == "POST":
        # Quando o formulário é enviado, você carrega os dados POST e FILES
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            # Salva as alterações no artigo
            form.save()
            return redirect('article_detail', pk=article.pk)
    else:
        # Quando você carrega a página de edição, a instância do artigo pré-preenche o formulário
        form = ArticleForm(instance=article)

    return render(request, 'app_project/article_form.html', {'form': form})


def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        article.delete()
        messages.success(request, 'Artigo excluído com sucesso!')  # Mensagem de sucesso na exclusão
        return redirect('article_list')

    return render(request, 'app_project/article_delete.html', {'article': article})

def search_view(request):
    query = request.GET.get('q')
    if query:
        # Busca pelo título, autores ou palavras-chave
        results = Article.objects.filter(
            Q(title__icontains=query) |
            Q(authors__icontains=query) |
            Q(keywords__icontains=query)
        )
    else:
        results = Article.objects.none()

    return render(request, 'app_project/search_results.html', {'results': results, 'query': query})


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

def article_update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            # Salva o estado atual do artigo no histórico antes de modificar
            ArticleHistory.objects.create(
                article=article,
                title=article.title,
                authors=article.authors,
                abstract=article.abstract,
                keywords=article.keywords
            )
            # Atualiza o artigo com os novos dados
            form.save()
            return redirect('article_detail', pk=article.pk)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'app_project/article_form.html', {'form': form})
