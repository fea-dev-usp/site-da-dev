from django.db import models
from django.contrib.auth.models import AbstractUser

class Posicao(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome

class Grupo(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.TextField(max_length=500, blank=True, null=True)
    reuniao = models.DateTimeField()

    def __str__(self):
        return self.nome

class Area(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.TextField(max_length=500, blank=True, null=True)
    reuniao = models.DateTimeField()

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    tipo = models.CharField(max_length=100)
    grupo = models.ManyToManyField(Grupo, related_name="projetos", blank=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name="projetos", blank=True, null=True)
    repositorio = models.URLField()

    def __str__(self):
        return self.tipo

class User(AbstractUser):
    posicao = models.ForeignKey(Posicao, on_delete=models.CASCADE, related_name="users", default=None, blank=True, null=True)
    grupo = models.ManyToManyField(Grupo, related_name="users", blank=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name="users", default=None, blank=True, null=True)
    n_usp = models.IntegerField(primary_key=True)
    data_nascimento = models.DateField()
    curso = models.CharField(max_length=100)
    foto = models.ImageField(upload_to="image/", blank=True, null=True)
    data_entrada = models.DateField()
    situacao = models.BooleanField()
    projetos = models.ManyToManyField(Projeto, related_name="users", blank=True)

    def __str__(self):
        return self.username

class Cargo(models.Model):
    cargo = models.CharField(max_length=30)
    semestre = models.DateField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cargos")

    def __str__(self):
        return f"{self.usuario}: {self.cargo}"

class Parceiro(models.Model):
    nome = models.CharField(max_length=100, primary_key=True)
    tipo = models.CharField(max_length=100)
    disponibilidade = models.CharField(max_length=100)
    email = models.EmailField()
    foto = models.ImageField()

    def __str__(self):
        return self.nome_parceiro

class Evento(models.Model):
    nome = models.CharField(max_length=100, primary_key=True)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    foto = models.ImageField()
    descricao = models.TextField()
    local = models.CharField(max_length=100)
    grupo = models.ManyToManyField(Grupo, related_name="eventos", blank=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name="eventos", blank=True, null=True)
    participantes = models.ManyToManyField(User, related_name="eventos", blank=True)

    def __str__(self):
        return self.nome

class Redes(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="redes_sociais")
    link = models.URLField()
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.usuario}: {self.nome}"
