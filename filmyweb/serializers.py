from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Film

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['']

class FilmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Film
        fields = [
            'id',
            'film_identyfikator',
            'film_tytul',
            'film_tytul_oryginalny',
            'film_rok_produkcji',
            'film_kraj_produkcji'
            'film_wersja_wyswietlania',
            'film_wersja_jezykowa',
            'film_gatunek',
            'film_dodatkowe'
        ]
