# Generated by Django 3.2.6 on 2021-08-14 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmyweb', '0033_alter_dystrybutor_gatunek'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dystrybutor',
            name='gatunek',
            field=models.PositiveSmallIntegerField(choices=[(3, 'Sci-fi'), (2, 'Komedia'), (6, 'Przygodowy'), (4, 'Drama'), (1, 'Horror'), (0, 'Inne'), (5, 'Akcja')], default=0),
        ),
    ]
