# Generated by Django 4.0.4 on 2022-04-21 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anime_app', '0012_posts_alter_comments_review_delete_reviews'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='review',
            new_name='post',
        ),
    ]
