# Generated by Django 2.2.13 on 2020-09-08 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200908_1846'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='id_cliente',
            new_name='cliente',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='id_instalacion',
            new_name='instalacion',
        ),
    ]