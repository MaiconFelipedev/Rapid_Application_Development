from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('welcome/', views.welcome, name='welcome'),
    path('eco/<str:texto>/', views.eco, name='eco'),
    path('info/', views.info, name='info'),
    path('user/', views.user, name='user'),
    path('contato/<str:fone>/', views.contato, name='contato'),
    path('', views.home, name='home')
]