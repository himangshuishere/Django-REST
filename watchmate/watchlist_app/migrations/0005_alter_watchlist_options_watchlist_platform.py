# Generated by Django 4.0 on 2022-01-11 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0004_streamplatform_watchlist_delete_movie'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='watchlist',
            options={'verbose_name': 'Watchlist', 'verbose_name_plural': 'Watchlists'},
        ),
        migrations.AddField(
            model_name='watchlist',
            name='platform',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='watchlist', to='watchlist_app.streamplatform'),
            preserve_default=False,
        ),
    ]