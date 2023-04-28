from django.urls import path
from .views import IndexTemplateView, FuncionariosListView


urlpatterns = [
    path('', IndexTemplateView.as_view()),
    path('funcionarios/', FuncionariosListView.as_view()),
]