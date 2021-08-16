from django.db.models import fields
from django.db.models.fields import files
from django.forms import ModelForm
from .models import Film, Dystrybutor2, Ocena

class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = [
            'film_tytul',
            'film_opis',
            'film_rok_produkcji',
            'film_plakat',
            'film_rezyseria',
            'film_scenaruisz',
            'film_kraj_produkcji',
            'film_video',
            'film_czas_trwania',
            'film_gatunek',
            'film_wersja_wyswietlania',
            'film_wersja_jezykowa',
            'film_identyfikator',
        ]

class DystrybutorForm(ModelForm):
    class Meta:
        model = Dystrybutor2
        fields = [
            'dys_nazwa',
            'dys_adres',
            'dys_nip',
        ]

class OcenaForm(ModelForm):
    class Meta:
        model = Ocena
        fields = ['gwiazdki', 'recenzja']

