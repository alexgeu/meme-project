# Generated by Django 3.0.5 on 2020-05-01 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myFirstApp', '0003_auto_20200412_1208'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemeImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgCaption', models.CharField(max_length=200)),
                ('meme_Main_Img', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
