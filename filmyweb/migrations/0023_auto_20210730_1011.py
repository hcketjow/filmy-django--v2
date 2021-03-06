# Generated by Django 3.2.4 on 2021-07-30 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmyweb', '0022_auto_20210730_1007'),
    ]

    operations = [
        migrations.RenameField(
            model_name='film',
            old_name='filmiki',
            new_name='url',
        ),
        migrations.AlterField(
            model_name='dodatkoweinfo',
            name='gatunek',
            field=models.PositiveSmallIntegerField(choices=[(6, 'Przygodowy'), (1, 'Horror'), (2, 'Komedia'), (5, 'Akcja'), (4, 'Drama'), (3, 'Sci-fi'), (0, 'Inne')], default=0),
        ),
    ]
