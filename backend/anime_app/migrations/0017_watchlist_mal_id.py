# Generated by Django 4.0.4 on 2022-04-21 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime_app', '0016_alter_watchlist_anime_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='mal_id',
            field=models.IntegerField(default=0),
        ),
    ]