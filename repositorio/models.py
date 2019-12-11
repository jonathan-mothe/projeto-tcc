# coding: utf-8
from django.db import models


class Autor(models.Model):
    nome = models.CharField(max_length=30, verbose_name='Nome')     
    ultimoNome = models.CharField(max_length=20, verbose_name='Último nome')
    matricula = models.CharField(max_length=12, verbose_name='Matrícula', unique=True)
    email = models.CharField(max_length=30, verbose_name='E-mail')        
    
    def __str__(self):
        return self.ultimoNome + ' ' + self.nome

class Aluno(Autor):

    def __str__(self):
        return self.ultimoNome + ' ' + self.nome

class Professor(Autor):

    def __str__(self):
        return self.ultimoNome + ' ' + self.nome

class Curso(models.Model):
    nome = models.CharField(max_length=30, verbose_name='Nome do Curso')
#    endereco = models.CharField(max_length=50, verbose_name='Endereço')
#    telefone = models.CharField(max_length=12, verbose_name='Telefone')

    def __str__(self):
        return self.nome

class Campus(models.Model):
    nome = models.CharField(max_length=30, verbose_name='Campus')
    sigla = models.CharField(max_length=30, verbose_name='Sigla')
    endereco = models.CharField(max_length=50, verbose_name='Endereço')
    telefone = models.CharField(max_length=12, verbose_name='Telefone')

    def __str__(self):
        return self.nome + '('+self.sigla+')'

class TipoTrabalho(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    descricao = models.CharField(max_length=100, verbose_name='descricao')

    def __str__(self):
        return self.nome

class Trabalho(models.Model):
    tipo = models.ForeignKey(TipoTrabalho, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100, verbose_name='Título')
    autor = models.ManyToManyField(Autor)
    orientador = models.ForeignKey(
        Professor,
        on_delete=models.CASCADE,
        related_name = '+'
    )
    palavraChave = models.CharField(max_length=200, verbose_name='Palavra Chave')
    abstract = models.TextField(verbose_name='Abstract')
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    dataPublicacao = models.DateField()
    pdf = models.FileField(verbose_name='PDF')
    def change_view(self):
        return self.pdf



