# Generated by Django 3.2.6 on 2021-08-16 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filmyweb', '0071_alter_film_film_wersja_jezykowa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='dodatkowe',
        ),
        migrations.AddField(
            model_name='film',
            name='dystrybutor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='filmyweb.dystrybutor'),
        ),
        migrations.AlterField(
            model_name='film',
            name='film_wersja_jezykowa',
            field=models.CharField(choices=[('Oryginalna', 'Oryginalna'), ('Dubbing', 'Dubbing'), ('Lektor', 'Lektor'), ('Napisy', 'Napisy')], default='', max_length=12),
        ),
        migrations.AlterField(
            model_name='film',
            name='film_wersja_wyswietlania',
            field=models.CharField(choices=[('2D', '2D'), ('3D', '3D')], default='', max_length=12),
        ),
    ]
