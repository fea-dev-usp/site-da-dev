from django.shortcuts import render
from django.core.paginator import Paginator

from .models import User, Grupo, Area, Cargo, Projeto, Evento, Parceiro, Posicao, Redes

# Create your views here.
def index(request):
    return render(request, 'feadev/index.html')

def sobre(request):
    return render(request, 'feadev/sobre.html')

def contato(request):
    return render(request, 'feadev/contato.html')

def projetos(request):
    projetos_lista = Projeto.objects.all()
    paginator = Paginator(projetos_lista, 6)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'feadev/projetos.html', {'projetos': page_obj})

def eventos(request):
    return render(request, 'feadev/eventos.html')

def grupos(request):
    return render(request, 'feadev/grupos.html')

def cursos(request):
    return render(request, 'feadev/cursos.html')

def processo_seletivo(request):
    return render(request, 'feadev/processo_seletivo.html')
