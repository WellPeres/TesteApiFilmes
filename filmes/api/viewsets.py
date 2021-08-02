from rest_framework import viewsets
from filmes.api import serializers
from filmes import models

class FilmesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.FilmesSerializer
    queryset = models.Filmes.objects.all()