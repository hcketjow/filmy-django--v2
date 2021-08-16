from django.contrib import admin
from .models import Film, Dystrybutor, Ocena, Aktor,Gatunek

# admin.site.register(Film)

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    # fields = ["tytul", "opis", "rok"]
    # exclude = ["opis"]
    list_display = ["film_tytul", "film_rok_produkcji"]
    search_fields = ("film_tytul", "film_opis")


admin.site.register(Gatunek)
admin.site.register(Dystrybutor)
admin.site.register(Ocena)
admin.site.register(Aktor)
