# Generated by Django 3.2.15 on 2022-09-01 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0005_alter_song_media'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.TextField(max_length=100),
        ),
    ]
