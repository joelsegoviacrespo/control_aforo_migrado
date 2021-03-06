# Generated by Django 2.2.13 on 2020-09-02 00:13

from django.db import migrations, models
import djongo.models.fields
import instalacion.forms
import instalacion.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Valores',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('instalacion', djongo.models.fields.EmbeddedField(blank=True, model_container=instalacion.models.InstalacionEmbebido, model_form_class=instalacion.forms.InstalacionEmbebidoForm, null=True)),
                ('descripcion', models.CharField(default='', max_length=255)),
                ('maximo_aforo', models.IntegerField(blank=True, default=0)),
                ('mostrar_valor', models.CharField(default='', max_length=255)),
                ('mostrar_capacidad', models.BooleanField(default=True)),
                ('mostrar_ambar', models.BooleanField(default=True)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'valores',
            },
        ),
    ]
