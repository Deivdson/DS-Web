from django.urls import path

from . import views

app_name = 'enquetes'
urlpatterns = [
    # ex.: /
    path('', views.IndexView.as_view(), name='index'),
    # ex.: /enquete/4/
    path('enquete/<int:pk>/', views.DetalhesView.as_view(), name='detalhes'),
    # ex.: /enquete/4/votacao/
    path('enquete/<int:id_enquete>/votacao/', views.votacao, name='votacao'),
    # ex.: /enquete/4/parcial/
    path('enquete/<int:pk>/parcial/', views.ResultadosView.as_view(), name='resultados'),
]