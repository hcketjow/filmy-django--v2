# Generated by Django 3.2.6 on 2021-08-15 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmyweb', '0037_alter_dystrybutor2_gatunek'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dystrybutor2',
            name='gatunek',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Inne'), (2, 'Komedia'), (1, 'Horror'), (6, 'Przygodowy'), (4, 'Drama'), (5, 'Akcja'), (3, 'Sci-fi')], default=0),
        ),
    ]
