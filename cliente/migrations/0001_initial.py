# Generated by Django 2.2.13 on 2020-08-27 19:41

from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('numero_cliente', models.CharField(default='', max_length=20)),
                ('nif', models.CharField(default='', max_length=20)),
                ('razon_social', models.CharField(default='', max_length=255)),
                ('direccion', models.CharField(default='', max_length=255)),
                ('poblacion', models.CharField(default='', max_length=255)),
                ('provincia', models.CharField(default='', max_length=255)),
                ('codigo_postal', models.CharField(default='', max_length=10)),
                ('contacto', models.CharField(default='', max_length=255)),
                ('cargo', models.CharField(default='', max_length=255)),
                ('telefono', models.CharField(default='', max_length=20)),
                ('movil', models.CharField(default='', max_length=20)),
                ('email', models.EmailField(default='', max_length=255)),
                ('administracion_nombre', models.CharField(default='', max_length=255)),
                ('administracion_cargo', models.CharField(default='', max_length=255)),
                ('administracion_telefono', models.CharField(default='', max_length=20)),
                ('administracion_movil', models.CharField(default='', max_length=20)),
                ('administracion_email', models.EmailField(default='', max_length=255)),
                ('tecnico_nombre', models.CharField(default='', max_length=255)),
                ('tecnico_cargo', models.CharField(default='', max_length=255)),
                ('tecnico_telefono', models.CharField(default='', max_length=20)),
                ('tecnico_movil', models.CharField(default='', max_length=20)),
                ('tecnico_email', models.EmailField(default='', max_length=255)),
                ('cliente_estado', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'cliente',
            },
        ),
    ]
