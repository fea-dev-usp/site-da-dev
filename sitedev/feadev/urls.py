from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sobre/", views.sobre, name="sobre"),
    path("contato/", views.contato, name="contato"),
    path("projetos/", views.projetos, name="projetos"),
    path("eventos/", views.eventos, name="eventos"),
    path("grupos/", views.grupos, name="grupos"),
    path("cursos/", views.cursos, name="cursos"),
    path("processo_seletivo/", views.processo_seletivo, name="processo_seletivo"),
]
