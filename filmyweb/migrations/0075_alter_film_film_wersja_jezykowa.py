# Generated by Django 3.2.6 on 2021-08-16 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmyweb', '0074_auto_20210816_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='film_wersja_jezykowa',
            field=models.CharField(choices=[('Oryginalna', 'Oryginalna'), ('Dubbing', 'Dubbing'), ('Napisy', 'Napisy'), ('Lektor', 'Lektor')], default='', max_length=12),
        ),
    ]
