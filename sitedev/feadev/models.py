from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    posicao = models.ForeignKey("Posicao", on_delete=models.CASCADE, related_name="user_position", default=None, blank=True, null=True)
    grupo = models.ManyToManyField("Grupo", on_delete=models.CASCADE, related_name="user_group", blank=True, null=True, default=None)
    area = models.ForeignKey("Area", on_delete=models.CASCADE, related_name="user_area", default=None, blank=True, null=True)
    n_usp = models.IntegerField(primary_key=True)
    data_nascimento = models.DateField()
    curso = models.CharField(max_length=100)
    foto = models.ImageField(upload_to="./media/image", blank=True, null=True)
    data_entrada = models.DateField()
    situacao = models.BooleanField()
    projetos = models.ManyToManyField("Projeto", on_delete=models.CASCADE, related_name="user_project", blank=True, null=True, default=None)

    def __str__(self):
        return f"{self.username}"

class Grupo(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.TextField(max_length=500, blank=True, null=True)
    reuniao = models.DateTimeField()

    def __str__(self):
        return f"{self.nome}"

class Area(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.TextField(max_length=500, blank=True, null=True)
    reuniao = models.DateTimeField()

    def __str__(self):
        return f"{self.nome}" 
    
class Cargo(models.Model):
    cargo = models.CharField(max_length=30)
    semestre = models.DateField()
    usuario = models.ForeignKey("User", on_delete=models.CASCADE, related_name="posicao_usuario")

    def __str__(self):
        return f"{self.usuario}: {self.cargo}"
    
class Projeto(models.Model):
    tipo = models.CharField(max_length=100)
    grupo = models.ManyToManyField("Grupo", on_delete=models.CASCADE, related_name="user_group", blank=True, null=True, default=None)
    area = models.ForeignKey("Area", on_delete=models.CASCADE, related_name="user_area", default=None, blank=True, null=True)
    repositorio = models.URLField()

    def __str__(self):
        return f"{self.repositorio}: {self.tipo}"
    
class Parceiro(models.Model):
    nome_parceiro = models.CharField(max_length=100, primary_key=True)
    tipo = models.CharField(max_length=100)
    disponibilidade = models.CharField(max_length=100)
    email = models.EmailField()
    foto = models.ImageField()

    def __str__(self):
        return f"{self.nome_parceiro}"

class Evento(models.Model):
    nome = models.CharField(max_length=100, primary_key=True)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    foto = models.ImageField()
    descricao = models.TextField()
    local = models.CharField(max_length=100)
    grupo = models.ManyToManyField("Grupo", on_delete=models.CASCADE, related_name="user_group", blank=True, null=True, default=None)
    area = models.ForeignKey("Area", on_delete=models.CASCADE, related_name="user_area", default=None, blank=True, null=True)
    participantes = models.ManyToManyField("User", on_delete=models.CASCADE, related_name="evento_participantes", blank=True, null=True, default=None)

    def __str__(self):
        return f"{self.nome}"
    
