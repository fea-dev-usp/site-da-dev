from django.forms import ModelForm
from .models import Contato, Membro, Categoria, Subcategoria


class ContatoForm(ModelForm):
    class Meta:
        model = Contato
        fields = '__all__'



class MembroForm(ModelForm):
    class Meta:
        model = Membro
        fields = '__all__'


class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'


class SubcategoriaForm(ModelForm):
    class Meta:
        model = Subcategoria
        fields = '__all__'
        