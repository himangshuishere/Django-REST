# Generated by Django 4.0 on 2022-01-27 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allNotes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notemodel',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
    ]
