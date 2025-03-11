from django.urls import path
from . import views

urlpatterns = [
    path('', views.livro_read, name='livro_read'),
    path('criar_livros/', views.livro_create, name='livro_create'),
    path('atualizar_livros/<int:pk>/', views.livro_update, name='livro_update'),
    path('apagar_livros/<int:pk>/', views.livro_delete, name='livro_delete'),
]