# Generated by Django 3.2.4 on 2021-07-30 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmyweb', '0024_auto_20210730_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dodatkoweinfo',
            name='gatunek',
            field=models.PositiveSmallIntegerField(choices=[(5, 'Akcja'), (4, 'Drama'), (2, 'Komedia'), (3, 'Sci-fi'), (1, 'Horror'), (0, 'Inne'), (6, 'Przygodowy')], default=0),
        ),
        migrations.AlterField(
            model_name='film',
            name='url_movie',
            field=models.URLField(default='', max_length=1000),
        ),
    ]
