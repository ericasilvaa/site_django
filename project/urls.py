from django.urls import path, include
from app_project import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Configuração para a documentação Swagger com drf-yasg
schema_view = get_schema_view(
   openapi.Info(
      title="API de Artigos",
      default_version='v1',
      description="Documentação da API para gerenciamento de artigos",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

# Definindo todas as rotas no mesmo urlpatterns
urlpatterns = [
    # Rotas principais do site
    path('admin/', admin.site.urls),
    path('', views.article_list, name='article_list'),  # Página inicial com a lista de artigos
    path('article/<int:pk>/', views.article_detail, name='article_detail'),  # Detalhes de um artigo específico
    path('article/new/', views.article_create, name='article_create'),  # Página para criar um novo artigo
    path('article/<int:pk>/edit/', views.article_update, name='article_update'),  # Página para editar um artigo
    path('article/<int:pk>/delete/', views.article_delete, name='article_delete'),  # Página para confirmar a exclusão
    path('search/', views.search_view, name='search'),

    # Rotas da API JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Rotas para os artigos da API
    path('api/artigos/', views.ArticleListCreateView.as_view(), name='article_list_create'),  # CRUD Artigos
    path('api/artigos/<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),

    # Documentação da API Swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
