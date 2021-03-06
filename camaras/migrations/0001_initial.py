# Generated by Django 2.2.13 on 2020-08-24 10:50

import camaras.models
from django.db import migrations, models
import djongo.models.fields
import instalacion.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camaras',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('instalacion', djongo.models.fields.EmbeddedField(blank=True, model_container=instalacion.models.InstalacionEmbebido, null=True)),
                ('nombre_camara', models.CharField(default='', max_length=250)),
                ('serial_camara', models.CharField(default='', max_length=250)),
                ('zonas_camara', djongo.models.fields.ArrayField(blank=True, model_container=camaras.models.ZonaCamara, null=True)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'camaras',
            },
        ),
    ]
