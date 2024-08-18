from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'feadev/index.html')

def sobre(request):
    return render(request, 'feadev/sobre.html')

def contato(request):
    return render(request, 'feadev/contato.html')

def projetos(request):
    return render(request, 'feadev/projetos.html')

def eventos(request):
    return render(request, 'feadev/eventos.html')

def grupos(request):
    return render(request, 'feadev/grupos.html')

def cursos(request):
    return render(request, 'feadev/cursos.html')

def processo_seletivo(request):
    return render(request, 'feadev/processo_seletivo.html')
