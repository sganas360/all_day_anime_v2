# Generated by Django 4.0.4 on 2022-04-20 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime_app', '0005_anime_alter_games_anime_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='title',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
