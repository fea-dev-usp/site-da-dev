from django.contrib import admin
from .models import User, Grupo, Area, Cargo, Projeto, Evento, Parceiro, Posicao, Redes

# Register your models here.
admin.site.register(User)
admin.site.register(Grupo)
admin.site.register(Area)
admin.site.register(Cargo)
admin.site.register(Projeto)
admin.site.register(Parceiro)
admin.site.register(Evento)
admin.site.register(Posicao)
admin.site.register(Redes)