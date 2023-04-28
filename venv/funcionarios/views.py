from django.shortcuts import render
from .models import Funcionario
from django.views.generic import TemplateView, ListView

app_name = 'funcionarios'

# Create your views here.
class IndexTemplateView(TemplateView):
    template_name = 'funcionarios/index.html'

class FuncionariosListView(ListView):
    template_name = 'funcionarios/lista.html'
    model = Funcionario
    context_object_name = 'funcionarios'

    
def index(request):
    # Primeiro, buscamos os funcionarios
    funcionarios = Funcionario.objetos.all()

    # Incluímos no contexto
    contexto = {
        'funcionarios': funcionarios
    }
    # Retornamos o template para listar os funcionários
    return render(request, 'funcionarios/index.html', contexto)