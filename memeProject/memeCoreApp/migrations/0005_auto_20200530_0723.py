# Generated by Django 3.0.4 on 2020-05-30 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('memeCoreApp', '0004_auto_20200524_0930'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meme',
            options={'ordering': ['-timestamp']},
        ),
    ]
