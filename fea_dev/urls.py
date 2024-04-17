"""fea_dev URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, re_path
from feadev import views 
from django.conf import settings


urlpatterns = [
    path('', views.index, name='index'),
    path('contato/', views.contato_view, name='contato'),
    path('membro_change_list/', views.membro_change_list_view, name='membro_change_list'),
    path('atividades/', views.atividades_view, name='atividades'),
    path('grupo_estudo/', views.grupo_estudo_view, name='grupo_estudo'), 
    path('index/trajetoria/', views.trajetoria_view, name='trajetoria'),
    path('index/valores/', views.valores_view, name='valores'),
    path('index/parcerias/', views.parcerias_view, name='parcerias'),
    path('index/estrutura/', views.estrutura_view, name='estrutura'),
    path('index/relatos/', views.relatos_view, name='relatos'),
    path('grupo_estudo/machine/', views.machine_view, name='machine'),
    path('grupo_estudo/f_quanticas/', views.f_quanticas_view, name='f_quanticas'),
    path('grupo_estudo/the_office/', views.the_office_view, name='the_office'),
    path('grupo_estudo/contagramacao/', views.contagramacao_view, name='contagramacao'),
    path('atividades/curso_python/', views.curso_python_view, name='curso_python'),
    path('atividades/conteudo/', views.conteudo_view, name='conteudo'),
    path('atividades/visitas/', views.visitas_view, name='visitas'),
    path("admin/", admin.site.urls),
]  





if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)