# Generated by Django 4.1.2 on 2022-10-09 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flix', '0003_movie_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='introduction',
            field=models.CharField(max_length=2000),
        ),
    ]