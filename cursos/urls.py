from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='cursos/login.html'), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('', views.curso_list, name='curso_list'),
    path('novo/', views.CursoCreate.as_view(), name='curso_create'),
    path('editar/<int:pk>/', views.CursoUpdate.as_view(), name='curso_update'),
    path('deletar/<int:pk>/', views.CursoDelete.as_view(), name='curso_delete'),
    path('chat/', views.chat_view, name='chat'),
]
