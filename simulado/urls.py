from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

from django.views.generic import TemplateView
from . import views

app_name = 'simulado'

urlpatterns = [
    path('',views.index.as_view(), name='index'),
    path('cadastro/', views.cadastro.as_view(), name='cadastro'),
    path('formSimulado/', views.formSimulado.as_view(), name='formSimulado'),
    path('detalhes/<int:pk>/', views.detalhes.as_view(), name='detalhes'),
    path('iniciarSimulado/<int:pk>/', views.iniciarSimulado.as_view(), name='iniciarSimulado'),
    path('resultado/<int:pk>/', views.resultado.as_view(), name='resultado'),
    path('login/', auth_views.LoginView.as_view(template_name='simulado/login.html'), name = 'login'),
    ]