# Generated by Django 3.2.6 on 2021-08-14 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmyweb', '0032_auto_20210814_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dystrybutor',
            name='gatunek',
            field=models.PositiveSmallIntegerField(choices=[(4, 'Drama'), (2, 'Komedia'), (0, 'Inne'), (5, 'Akcja'), (3, 'Sci-fi'), (6, 'Przygodowy'), (1, 'Horror')], default=0),
        ),
    ]