# Generated by Django 3.2.6 on 2021-08-15 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filmyweb', '0035_alter_dystrybutor_gatunek'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dystrybutor2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('czas_trwania', models.PositiveSmallIntegerField(default=0)),
                ('gatunek', models.PositiveSmallIntegerField(choices=[(2, 'Komedia'), (1, 'Horror'), (0, 'Inne'), (5, 'Akcja'), (3, 'Sci-fi'), (4, 'Drama'), (6, 'Przygodowy')], default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='film',
            name='dodatkowe',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='filmyweb.dystrybutor2'),
        ),
        migrations.DeleteModel(
            name='Dystrybutor',
        ),
    ]
