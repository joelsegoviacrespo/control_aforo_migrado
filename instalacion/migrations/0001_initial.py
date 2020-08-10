# Generated by Django 2.2.13 on 2020-07-14 12:57

from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instalacion',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('nombre_comercial', models.CharField(default='', max_length=255)),
                ('direccion', models.CharField(default='', max_length=255)),
                ('telefono', models.CharField(default='', max_length=20)),
                ('movil', models.CharField(default='', max_length=20)),
                ('email', models.CharField(default='', max_length=255)),
                ('poblacion', models.CharField(default='', max_length=255)),
                ('provincia', models.CharField(default='', max_length=255)),
                ('codigo_postal', models.CharField(default='', max_length=10)),
                ('contacto_nombre', models.CharField(default='', max_length=255)),
                ('contacto_cargo', models.CharField(default='', max_length=255)),
                ('contacto_telefono', models.CharField(default='', max_length=20)),
                ('contacto_movil', models.CharField(default='', max_length=20)),
                ('contacto_email', models.CharField(default='', max_length=255)),
                ('tecnico_nombre', models.CharField(default='', max_length=255)),
                ('tecnico_cargo', models.CharField(default='', max_length=255)),
                ('tecnico_telefono', models.CharField(default='', max_length=20)),
                ('tecnico_movil', models.CharField(default='', max_length=20)),
                ('tecnico_email', models.CharField(default='', max_length=255)),
                ('instalacion_estado', models.BooleanField(default=True)),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.Cliente')),
            ],
        ),
    ]
