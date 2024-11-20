from django.urls import path
<<<<<<< HEAD
=======
from django.contrib.auth import views as auth_views  # Importando as views de autenticação
>>>>>>> Parte 3
from .views import ArticleListCreateView, ArticleDetailView

urlpatterns = [
    path('articles/', ArticleListCreateView.as_view(), name='article-list-create'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
<<<<<<< HEAD
=======
    #path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # Adicionando URL de login
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Adicionando URL de logout
>>>>>>> Parte 3
]
