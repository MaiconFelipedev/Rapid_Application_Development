from django.urls import path
from . import views

urlpatterns = [
    path('autores/', views.autor_list, name='autor_list'),
    path('autores/novo/', views.autor_create, name='autor_create'),
    path('autores/editar/<int:id>/', views.autor_update, name='autor_update'),
    path('autores/excluir/<int:id>/', views.autor_delete, name='autor_delete'),

    path('editoras/', views.editora_list, name='editora_list'),
    path('editoras/nova/', views.editora_create, name='editora_create'),
    path('editoras/editar/<int:id>/', views.editora_update, name='editora_update'),
    path('editoras/excluir/<int:id>/', views.editora_delete, name='editora_delete'),

    path('livros/', views.livro_list, name='livro_list'),
    path('livros/novo/', views.livro_create, name='livro_create'),
    path('livros/editar/<int:id>/', views.livro_update, name='livro_update'),
    path('livros/excluir/<int:id>/', views.livro_delete, name='livro_delete'),

    path('publicacoes/', views.publica_list, name='publica_list'),
    path('publicacoes/nova/', views.publica_create, name='publica_create'),
    path('publicacoes/editar/<int:id>/', views.publica_update, name='publica_update'),
    path('publicacoes/excluir/<int:id>/', views.publica_delete, name='publica_delete'),
]