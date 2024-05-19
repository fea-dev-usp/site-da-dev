from django.db import models



class Contato(models.Model):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    mensagem= models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
 


CATEGORIA_CHOICES = (
        ('Fundadores', 'Fundadores'),
        ('Presidência', 'Presidência'),
        ('Vice-Presidência', 'Vice-Presidência'),
        ('Área Administrativa', 'Área Administrativa')

)


class Categoria(models.Model):
    categoria = models.CharField(max_length=255, choices=CATEGORIA_CHOICES, blank=True, null=True, verbose_name="Categoria")
    nova_categoria = models.CharField(max_length=255, blank=True, null=True, verbose_name="Nova Categoria")

    def __str__(self):
        if self.categoria:
            return self.categoria
        else:
            return self.nova_categoria

    def save(self, *args, **kwargs):
        if self.nova_categoria and not self.categoria:
            self.categoria = self.nova_categoria
        super(Categoria, self).save(*args, **kwargs)    
        
    class Meta:
        verbose_name_plural = "Categorias"

        
        






SUBCATEGORIA_CHOICES = (
    ('IA', 'IA'),
    ('RH', 'RH'),
    ('Projetos', 'Projetos'),
    ('FinQuant', 'FinQuant'),
    ('Marketing', 'Marketing'),
    ('The Office', 'The Office'),
    ('Contagramação', 'Contagramação'),
    ('Machine Learning', 'Machine Learning'),    
)

class Subcategoria(models.Model):
    sub_categoria = models.CharField(max_length=255, choices=SUBCATEGORIA_CHOICES, blank=True, null=True, verbose_name="Subcategoria")
    nova_subcategoria = models.CharField(max_length=255, blank=True, null=True, verbose_name="Nova Subcategoria")

    def __str__(self):
        if self.sub_categoria:
            return self.sub_categoria
        else:
            return self.nova_subcategoria
        
    def save(self, *args, **kwargs):
        if self.nova_subcategoria and not self.sub_categoria:
            self.sub_categoria = self.nova_subcategoria
        super(Subcategoria, self).save(*args, **kwargs)
        
    class Meta:
        verbose_name_plural = "Subcategorias"







class Membro(models.Model):
    nome = models.CharField(max_length=255, verbose_name="Nome")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Categoria")
    sub_categoria = models.ForeignKey(Subcategoria, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Subcategoria")
    ativo = models.BooleanField(default=False, null=False)
    inativo = models.BooleanField(default=False, null=False)
    info = models.TextField(max_length=320)
    imagem = models.ImageField(upload_to='membros', null=True, blank=True)
    ano = models.IntegerField(default=2023)

    def __str__(self):
        return self.nome
    class Meta:
        verbose_name_plural = "Membros"

