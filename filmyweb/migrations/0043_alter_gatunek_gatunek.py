# Generated by Django 3.2.6 on 2021-08-15 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmyweb', '0042_alter_film_gatunek'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gatunek',
            name='gatunek',
            field=models.CharField(default=0, max_length=150),
        ),
    ]