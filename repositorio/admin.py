# coding: utf-8
from django.contrib import admin
from repositorio.models import *

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    search_fields = ['nome', 'ultimoNome']
    list_display = ['nome', 'matricula', 'email']  # Fim da classe

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    search_fields = ['nome', 'ultimoNome']
    list_display = ['nome', 'matricula', 'email']  # Fim da classe

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    list_display = ['nome']  # Fim da classe

@admin.register(TipoTrabalho)
class TipoTrabalhoAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    list_display = ['nome', 'descricao'] # Fim da classe

@admin.register(Campus)
class CampusAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    list_display = ['nome', 'endereco', 'telefone']  # Fim da classe


@admin.register(Trabalho)
class TrabalhoAdmin(admin.ModelAdmin):
    search_fields = ['autor__nome', 'tipo__nome', 'orientador__nome', 'titulo'] #('titulo', 'orientador', 'autor__nome',)
    list_display = ['autores', 'titulo', 'tipo', 'orientador', 'dataPublicacao', 'pdf']
    list_filter = ('tipo', 'campus')
    def autores(self, obj):
        return ", ".join([a.nome + ' ' + a.ultimoNome for a in obj.autor.all()])



