# Generated by Django 2.2.13 on 2020-09-18 01:43

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
            name='Posicion',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('instalacion', djongo.models.fields.EmbeddedField(blank=True, model_container=instalacion.models.InstalacionEmbebido, model_form_class=instalacion.forms.InstalacionEmbebidoForm, null=True)),
                ('posicion_reloj', models.IntegerField(blank=True, default=0)),
                ('color', models.CharField(default='', max_length=20)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'posicion',
            },
        ),
    ]
