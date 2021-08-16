from django.core import serializers
from django.core.serializers import serialize
from django.shortcuts import render, get_object_or_404, redirect
from .models import Film, Dystrybutor2, Ocena
from .forms import FilmForm, DystrybutorForm, OcenaForm
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer, FilmSerializer 
from django.db.models import Q
from django.core.paginator import EmptyPage, PageNotAnInteger,Paginator
from django.http import HttpResponse
from django.contrib.auth.models import User
import xlwt

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FilmView(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

def wszystkie_filmy(request):
    wszystkie = Film.objects.all()
    query = request.GET.get('q')
    rok_powstania = request.GET.get('rok')    
    rezyseria_szukaj = request.GET.get('rezyser')
    filmy_szukaj = request.GET.get('film_szuk')
    scenariusz_szukaj = request.GET.get('scen_szukaj')

    if query:
        wszystkie = Film.objects.filter(
            Q(film_tytul__icontains=query) | Q(film_rok_produkcji__icontains=query) |
            Q(film_rezyseria__icontains=query) | Q(film_scenaruisz__icontains=query) |
            Q(film_kraj_produkcji__icontains=query)
        ).distinct()
    if rok_powstania:
        wszystkie = Film.objects.filter(film_rok_produkcji__icontains=rok_powstania).distinct()
    if rezyseria_szukaj:
        wszystkie = Film.objects.filter(film_rezyseria__icontains=rezyseria_szukaj).distinct()
    if filmy_szukaj:
        wszystkie = Film.objects.filter(film_tytul__icontains=filmy_szukaj).distinct()
    if scenariusz_szukaj:
        wszystkie = Film.objects.filter(film_scenaruisz__icontains=scenariusz_szukaj).distinct()


    paginator = Paginator(wszystkie,6)
    page = request.GET.get('page')

    try: 
        films = paginator.page(page)
    except PageNotAnInteger: 
        films = paginator.page(1)
    except EmptyPage: 
        films = paginator.page(paginator.num_pages)

    context={
        'filmy': films,
    }
    
    return render(request, 'filmy.html', context)

@login_required
def nowy_film(request):
    form_film = FilmForm(request.POST or None, request.FILES or None)
    form_dodatkowe = DystrybutorForm(request.POST or None)

    if all((form_film.is_valid(), form_dodatkowe.is_valid())):
        film = form_film.save(commit=False)
        dodatkowe = form_dodatkowe.save()
        film.dodatkowe = dodatkowe
        film.save()
        return redirect(wszystkie_filmy)

    return render(request, 'film_form.html', {
        'form': form_film,
        'form_dodatkowe': form_dodatkowe,
        'oceny': None,
        'form_ocena': None, 
        'nowy': True,
    })

@login_required
def edytuj_film(request, id):
    film = get_object_or_404(Film, pk=id)
    oceny = Ocena.objects.filter(film=film)
    # aktorzy = film.aktorzy.all()

    try:
        dodatkowe = Dystrybutor2.objects.get(film=film.id)
    except Dystrybutor2.DoesNotExist:
        dodatkowe = None

    form_film = FilmForm(request.POST or None, request.FILES or None, instance=film)
    form_dodatkowe = DystrybutorForm(request.POST or None, instance=dodatkowe)
    form_ocena = OcenaForm(None)

    if request.method == "POST":
        if 'gwiazdki' in request.POST:
            ocena = form_ocena.save(commit=False)
            ocena.film = film
            ocena.save()

    if all((form_film.is_valid(), form_dodatkowe.is_valid())):
        film = form_film.save(commit=False)
        dodatkowe = form_dodatkowe.save()
        film.dodatkowe = dodatkowe
        film.save()
        return redirect(wszystkie_filmy)

    return render(request, 'film_form.html', {
        'form': form_film,
        'form_dodatkowe': form_dodatkowe,
        'oceny': oceny,
        'form_ocena': form_ocena,
        'nowy': False})

@login_required
def usun_film(request, id):
    film = get_object_or_404(Film, pk=id)

    if request.method == "POST":
        film.delete()
        return redirect(wszystkie_filmy)

    return render(request, 'potwierdz.html', {'film': film})

@login_required
def lista_film(request):
    lista = Film.objects.all()
    szukaj = request.GET.get('q')

    if szukaj:
        lista = Film.objects.filter(
            Q(film_tytul__icontains=szukaj) | Q(film_rok_produkcji__icontains=szukaj) |
            Q(film_rezyseria__icontains=szukaj) | Q(film_scenaruisz__icontains=szukaj) |
            Q(film_kraj_produkcji__icontains=szukaj)
        ).distinct()

    paginator = Paginator(lista,6)
    page = request.GET.get('page')
    try: 
        lists = paginator.page(page)
    except PageNotAnInteger: 
        lists = paginator.page(1)
    except EmptyPage: 
        lists = paginator.page(paginator.num_pages)

    context={
        'lista': lists,
    }


    return render(request, 'lista.html',context)


def export_xml(request):
    queryset = Film.objects.all()
    queryset = serializers.serialize('xml',queryset)
    return HttpResponse(queryset, content_type="application/xml")


def export_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="filmy.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Filmy') # this will make a sheet named Users Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = [
        'Id'
        'Identyfikator',
        'Tytuł',
        'Tytuł_oryginalny',
        'Kraj_produkcji',
        'Wesja_wyświelteniowa',
        'Wersja_jęzkowa',
        'Gatunek',
        'Dystrybutor',
    ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Film.objects.all().values_list(
        'id',
        'film_identyfikator'
        'film_tytul',
        'film_tytul_oryginalny',
        'film_rok_produkcji',
        'film_kraj_produkcji',
        'film_opis',
        'film_rezyseria',
        'film_scenaruisz',
        'film_produkcja'
    )
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    return response




# Create
# Read
# Update
# Delete