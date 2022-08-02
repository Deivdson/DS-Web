from django.urls import path

from . import views
from django.views.generic import TemplateView

app_name='cronograma'
urlpatterns = [
    path('', views.index, name='index'),
    path('dayleSchedule/<int:pk>/', views.detalhes, name='detalhes'),
    path('dayleSchedule/NovoCronograma/', views.cronogramaForm.as_view(), name='cronogramaForm'),
]