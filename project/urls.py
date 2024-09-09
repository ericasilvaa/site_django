 
from django.urls import path
from app_project import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # rota, view reponsavel , nome referencia 
    #exe: usuario.com 
    #path('',views.home, name='home'),
    
    path('', views.article_list, name='article_list'), #Página inicial com a lista de artigos
    path('article/<int:pk>/', views.article_detail, name='article_detail'), # Detalhes de um artigo específico
    path('article/new/', views.article_create, name='article_create'), # Pg para criar um novo artigo
    path('article/<int:pk>/edit/', views.article_update, name='article_update'), # Pg para editar 
    path('article/<int:pk>/delete/', views.article_delete, name='article_delete'),# Pg para confirmar a exclusão 
    path('search/', views.search_view, name='search'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
