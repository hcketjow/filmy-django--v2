# Generated by Django 3.2.6 on 2021-08-15 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmyweb', '0047_alter_gatunek_gatunek'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gatunek',
            name='gatunek',
            field=models.PositiveSmallIntegerField(choices=[], max_length=150),
        ),
    ]
