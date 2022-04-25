# Generated by Django 4.0.4 on 2022-04-21 18:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('anime_app', '0018_alter_watchlist_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='list', to=settings.AUTH_USER_MODEL),
        ),
    ]
