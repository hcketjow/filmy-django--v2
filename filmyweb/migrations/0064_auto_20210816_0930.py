# Generated by Django 3.2.6 on 2021-08-16 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmyweb', '0063_auto_20210816_0922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='film_produkcja',
        ),
        migrations.AlterField(
            model_name='film',
            name='film_wersja_jezykowa',
            field=models.CharField(choices=[('Lektor', 'Lektor'), ('Oryginalna', 'Oryginalna'), ('Dubbing', 'Dubbing'), ('Napisy', 'Napisy')], default='', max_length=12),
        ),
        migrations.AlterField(
            model_name='film',
            name='film_wersja_wyswietlania',
            field=models.CharField(choices=[('2D', '2D'), ('3D', '3D')], default='', max_length=12),
        ),
    ]
