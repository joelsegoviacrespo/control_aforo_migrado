# Generated by Django 2.2.13 on 2020-08-28 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='rol',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Superusuario'), (2, 'Administrador'), (3, 'Usuario')], default=0),
        ),
    ]
