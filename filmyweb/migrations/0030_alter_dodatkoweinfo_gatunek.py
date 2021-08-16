# Generated by Django 3.2.4 on 2021-07-30 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmyweb', '0029_alter_dodatkoweinfo_gatunek'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dodatkoweinfo',
            name='gatunek',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Inne'), (1, 'Horror'), (2, 'Komedia'), (3, 'Sci-fi'), (5, 'Akcja'), (4, 'Drama'), (6, 'Przygodowy')], default=0),
        ),
    ]