from django.shortcuts import render
from .models import Funcionario
from django.views.generic import ListView

# Create your views here.
class ListaFuncionarios(ListView):
    template_name = 'funcionarios/index.html'
    model = Funcionario
    context_object_name = 'funcionarios'

    
# def index(request):
#     funcionarios = Funcionario.objetos.all()

#     contexto = {
#         'funcionarios': funcionarios
#     }
    
#     return render(request, 'funcionarios/index.html', contexto)