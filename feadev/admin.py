from django.contrib import admin
admin.site.site_header = 'Administração do site'
from .models import Contato, Membro, Categoria, Subcategoria
from django.utils.html import format_html



admin.site.register(Contato)
actions = ['mark_as_read', 'mark_as_unread']
admin.site.add_action('mark_as_read', 'Marcar como lido')
admin.site.add_action('mark_as_unread', 'Marcar como não lido')




class MembroAdmin(admin.ModelAdmin):
    actions = ['ativar_membros', 'desativar_membros']
    list_filter = ['categoria',  'sub_categoria', 'ativo', 'inativo','ano']
    list_display = ['nome', 'categoria', 'sub_categoria', 'status', 'imagem_thumbnail']

    def ativar_membros(self, request, queryset):
        queryset.update(ativo=True)
        request.session['ativo'] = True

    def desativar_membros(self, request, queryset):
        queryset.update(ativo=False)
        request.session['inativo'] = False

    def imagem_thumbnail(self, obj):
        if obj.imagem:
            return format_html('<img src="{}" width="40" height="40" />', obj.imagem.url)
        else:
            return ''
    imagem_thumbnail.short_description = 'Imagem'


    

    def status(self, obj):
        if obj.ativo:
            return 'Ativo'
        elif obj.inativo:
            return 'Inativo'
        else:
            return 'N/A'

    status.short_description = 'Status'

admin.site.register(Membro, MembroAdmin)




class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('categoria', 'nova_categoria')
    
admin.site.register(Categoria)





class SubcategoriaAdmin(admin.ModelAdmin):
    list_display = ('sub_categoria', 'nova_subcategoria')

admin.site.register(Subcategoria)
