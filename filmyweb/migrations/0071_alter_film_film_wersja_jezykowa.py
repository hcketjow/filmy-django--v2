# Generated by Django 3.2.6 on 2021-08-16 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmyweb', '0070_alter_film_film_wersja_jezykowa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='film_wersja_jezykowa',
            field=models.CharField(choices=[('Napisy', 'Napisy'), ('Dubbing', 'Dubbing'), ('Lektor', 'Lektor'), ('Oryginalna', 'Oryginalna')], default='', max_length=12),
        ),
    ]
