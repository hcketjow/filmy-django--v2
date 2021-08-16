from django.db import models
from embed_video.fields import EmbedVideoField

class Dystrybutor(models.Model):
    dys_nazwa = models.CharField(max_length=50,default="")
    dys_adres = models.CharField(max_length=500, default="")
    dys_nip = models.CharField(max_length=10, default="")
    
    def __str__(self):
        return self.dys_nazwa

class Gatunek(models.Model):
    gatunek = models.CharField(blank=True, max_length=150)
    
    def __str__(self):
        return self.gatunek

class Kraj_produkcji(models.Model):
    kraj_produkcji = models.CharField(blank=True, max_length=150)
    
    def __str__(self):
        return self.kraj_produkcji

class Film(models.Model):
    WERSJA = {
        ('2D', '2D'),
        ('3D', '3D'),
    }
    JEZYK = {
        ('Dubbing', 'Dubbing'),
        ('Lektor', 'Lektor'),
        ('Napisy', 'Napisy'), 
        ('Oryginalna', 'Oryginalna'),
    }
    film_tytul = models.CharField(max_length=64, blank=False, unique=True) 
    film_tytul_oryginalny = models.CharField(max_length=64,default="", unique=True) 
    film_rok_produkcji = models.PositiveSmallIntegerField(default=2000)
    film_opis = models.TextField(default="", max_length=1000)
    film_plakat = models.ImageField(upload_to="plakaty", null=True, blank=True)
    dystrybutor = models.ForeignKey(Dystrybutor, on_delete=models.CASCADE, null=True, blank=True)
    film_rezyseria = models.CharField(default="", max_length=100)
    film_scenaruisz = models.CharField(default="", max_length=100)
    film_kraj_produkcji = models.ForeignKey(Kraj_produkcji, on_delete=models.CASCADE, null=True, blank=True)
    film_video = EmbedVideoField(default="")
    film_czas_trwania = models.PositiveSmallIntegerField(default=0)
    film_gatunek = models.ForeignKey(Gatunek, on_delete=models.CASCADE, null=True, blank=True)
    film_identyfikator = models.CharField(default="", max_length=200)
    film_wersja_wyswietlania = models.CharField(max_length=12,default="",choices=WERSJA)
    film_wersja_jezykowa = models.CharField(max_length=12,default="",choices=JEZYK)

    def __str__(self):
        return self.tytul_z_rokiem()

    def tytul_z_rokiem(self):
        return "{} ({})".format(self.film_tytul, self.film_rok_produkcji)

class Ocena(models.Model):
    recenzja = models.TextField(default="", blank=True)
    gwiazdki = models.PositiveSmallIntegerField(default=5)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)

class Aktor(models.Model):
    imie = models.CharField(max_length=32)
    nazwisko = models.CharField(max_length=32)
    filmy = models.ManyToManyField(Film, related_name="aktorzy")

