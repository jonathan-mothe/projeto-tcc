from rest_framework import serializers, viewsets
from rest_framework import generics
from repositorio.models import *
from repositorio.serializers import *
#import django_filters.rest_framework
from rest_framework.filters import SearchFilter


class TrabalhoList(viewsets.ModelViewSet):
    queryset = Trabalho.objects.all()
    serializer_class = TrabalhoSerializer
    http_method_names = ['get']
    filter_backends = (SearchFilter,)
    search_fields = (
        'tipo__nome',
        'titulo',
        'autor__nome',
        'autor__ultimoNome',
        'orientador__nome',
        'palavraChave',
        'curso__nome',
        'campus__nome',
    )
    filter_fields = (
        'tipo',
        'titulo',
        'autor',
        'orientador',
        'palavraChave',
        'curso',
        'campus',
        'dataPublicacao',
    )
    def get_queryset(self, *args, **kwargs):
        queryset = Trabalho.objects.all()
        tipo_id = self.request.GET.get('tipo_pk')
        autor_id = self.request.GET.get('autor_pk')
        curso_id = self.request.GET.get('curso_pk')
        
        if tipo_id is not None:
            return self.queryset.filter(tipo_id=tipo_id)
        elif autor_id is not None:
            return self.queryset.filter(autor__in=[autor_id])
        elif curso_id is not None:
            return self.queryset.filter(curso_id=curso_id)
        else:
            return queryset               

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get']