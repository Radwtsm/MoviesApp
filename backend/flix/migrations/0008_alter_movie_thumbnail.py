# Generated by Django 4.1.2 on 2022-10-10 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flix', '0007_alter_movie_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='thumbnail',
            field=models.ImageField(upload_to='files/thumbnails'),
        ),
    ]