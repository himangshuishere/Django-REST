# Generated by Django 4.0 on 2022-01-07 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'verbose_name': 'Movie List', 'verbose_name_plural': 'Movies List'},
        ),
    ]
