from django.contrib.auth.models import User
from repositorio.views import *
from repositorio.models import * 

class AutorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Autor
        fields = (
            'id',
            'nome',
            'ultimoNome',
            'matricula',
            'email',
        )

class ProfessorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Professor
        fields = (
            'id',
            'nome',
            'ultimoNome',
            'matricula',
            'email',
        )

class CursoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Curso
        fields = (
            'id',
            'nome',
        )

class CampusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Campus
        fields = (
            'id',
            'nome',
            'sigla',
            'endereco',
            'telefone',
        )

class TipoTrabalhoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoTrabalho
        fields = (
            'id',
            'nome',
            'descricao'
        )

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'email', 'is_staff')


class TrabalhoSerializer(serializers.HyperlinkedModelSerializer):
    autor = AutorSerializer(many=True, read_only=True)
    tipo = TipoTrabalhoSerializer(many=False, read_only=True)
    orientador = ProfessorSerializer(many=False, read_only=True)
    curso = CursoSerializer(read_only=True)
    campus = CampusSerializer(many=False, read_only=True)

    class Meta:
        model = Trabalho
        fields = (
            'id',
            'tipo',
            'titulo',
            'autor',
            'orientador',
            'palavraChave',
            'curso',
            'campus',
            'dataPublicacao',
            'pdf',
        )