# Generated by Django 4.0.4 on 2022-04-21 17:29

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('anime_app', '0014_alter_watchlist_anime_title'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='watchlist',
            unique_together={('creator', 'anime_title')},
        ),
    ]
