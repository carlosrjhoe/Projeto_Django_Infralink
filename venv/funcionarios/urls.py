from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListaFuncionarios.as_view()),
]