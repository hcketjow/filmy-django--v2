# Generated by Django 3.2.6 on 2021-08-16 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmyweb', '0057_alter_gatunek_gatunek'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gatunek',
            name='gatunek',
            field=models.CharField(default='', max_length=150),
        ),
    ]
