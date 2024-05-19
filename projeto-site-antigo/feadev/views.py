from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContatoForm
from django.views.decorators.csrf import csrf_protect
from .models import Membro, Categoria, Subcategoria


def index(request):
    return render(request, 'index.html')


def estrutura_view(request):
    return render(request, 'estrutura.html')


def trajetoria_view(request):
    return render(request, 'trajetoria.html')


def membro_change_list_view(request):
    membros = Membro.objects.all()
    categorias = Categoria.objects.values_list('categoria', flat=True).distinct()
    sub_categorias = Subcategoria.objects.values_list('sub_categoria', flat=True).distinct()
    anos = Membro.objects.values_list('ano', flat=True).distinct()
    contexto = {
        'anos': anos,
        'membros': membros,
        'categorias': categorias,
        'sub_categorias': sub_categorias,
    }

    anos_unicos = sorted(set(anos))

    contexto = {
        'membros': membros,
        'categorias': categorias,
        'sub_categorias': sub_categorias,
        'anos_unicos': anos_unicos,  
    }

    return render(request, 'membro_change_list.html', contexto)


def atividades_view(request):
    return render(request, 'atividades.html')

def valores_view(request):
    return render(request, 'valores.html')

def relatos_view(request):
    return render(request, 'relatos.html')

def grupo_estudo_view(request):
    return render(request, 'grupo_estudo.html')

def parcerias_view(request):
    return render(request, 'parcerias.html')

def curso_python_view(request):
    return render(request, 'curso_python.html')

def conteudo_view(request):
    return render(request, 'conteudo.html')

def visitas_view(request):
    return render(request, 'visitas.html')

def grupo_estudo_view(request):
    return render(request, 'grupo_estudo.html')

def machine_view(request):
    return render(request, 'machine.html')

def f_quanticas_view(request):
    return render(request, 'f_quanticas.html')

def the_office_view(request):
    return render(request, 'the_office.html')

def contagramacao_view(request):
    return render(request, 'contagramacao.html')




@csrf_protect

def contato_view(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            mensagem = form.cleaned_data['mensagem']
            email_subject = f'Novo contato de {nome}'
            email_message = f'Mensagem de {email}:\n\n{mensagem}'

            send_mail(
                email_subject,
                email_message,
                settings.DEFAULT_FROM_EMAIL, 
                [settings.EMAIL_HOST_USER],  
            )

            return render(request, 'index.html')
    else:
        form = ContatoForm()
    context = {'form': form}
    return render(request, 'contato.html', context)
