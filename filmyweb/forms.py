from django import forms
from django.db.models import fields
from django.db.models.fields import files
from django.forms import ModelForm
from .models import Film, Dystrybutor, Ocena

class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = [
            'film_tytul',
            'film_tytul_oryginalny',
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
            'dystrybutor',
        ]
        widgets = {
            'film_tytul':forms.TextInput(attrs={'placeholder':'Podaj tytuł'}),
            'film_opis':forms.Textarea(attrs={'placeholder':'Podaj opis'}),
            'film_rok_produkcji':forms.TextInput(attrs={'placeholder':'Podaj Rok produkcji'}),
            'film_tytul_oryginalny':forms.TextInput(attrs={'placeholder':'Podaj tytuł oryginalny'}),
            'film_rezyseria':forms.TextInput(attrs={'placeholder':'Podaj reżysera'}),
            'film_scenaruisz':forms.TextInput(attrs={'placeholder':'Podaj scenarzyste'}),
            'film_kraj_produkcji':forms.TextInput(attrs={'placeholder':'Podaj kraj produkcji'}),
            'film_video':forms.TextInput(
                attrs={
                    'placeholder':'Podaj video do wyświetlenia',
                    
                }),
            'film_identyfikator':forms.TextInput(attrs={'placeholder':'Podaj identydikator'}),
        }

class DystrybutorForm(ModelForm):
    class Meta:
        model = Dystrybutor
        fields = [
            'dys_nazwa',
            'dys_adres',
            'dys_nip',
        ]
        widgets = {
            'dys_nazwa':forms.TextInput(attrs={'placeholder':'Podaj nazwę dystrybutora'}),
            'dys_adres':forms.TextInput(attrs={'placeholder':'Podaj adres dystrybutora'}),
            'dys_nip':forms.TextInput(attrs={'placeholder':'Podaj nip dystrybutora'}),
        }

class OcenaForm(ModelForm):
    class Meta:
        model = Ocena
        fields = ['gwiazdki', 'recenzja']

