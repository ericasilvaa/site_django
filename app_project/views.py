#from django.shortcuts import render
#def home (request):
#    return render(request,'usuarios/home.html')

from django.shortcuts import render, get_object_or_404, redirect
from django.template import TemplateDoesNotExist
from .models import Article
from .forms import ArticleForm
from django.contrib import messages

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
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, 'Artigo atualizado com sucesso!')  # Mensagem de sucesso na atualização
            return redirect('article_detail', pk=article.pk)
        else:
            messages.error(request, 'Erro ao atualizar o artigo. Verifique os dados informados.')  # Mensagem de erro
    else:
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
    # Lógica de busca
    return render(request, 'app_project/search_results.html')