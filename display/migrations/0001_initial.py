# Generated by Django 2.2.13 on 2020-09-20 22:56

from django.db import migrations, models
import djongo.models.fields
import espacios.forms
import espacios.models
import fondos.forms
import fondos.models
import instalacion.forms
import instalacion.models
import posicion.forms
import posicion.models
import valores.forms
import valores.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Display',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('instalacion', djongo.models.fields.EmbeddedField(blank=True, model_container=instalacion.models.InstalacionEmbebido, model_form_class=instalacion.forms.InstalacionEmbebidoForm, null=True)),
                ('descripcion', models.CharField(default='', max_length=255)),
                ('valores', djongo.models.fields.EmbeddedField(blank=True, model_container=valores.models.ValoresEmbebido, model_form_class=valores.forms.ValoresEmbebidoForm, null=True)),
                ('fondos', djongo.models.fields.EmbeddedField(blank=True, model_container=fondos.models.FondosEmbebido, model_form_class=fondos.forms.FondosEmbebidoForm, null=True)),
                ('posicion', djongo.models.fields.EmbeddedField(blank=True, model_container=posicion.models.PosicionEmbebido, model_form_class=posicion.forms.PosicionEmbebidoForm, null=True)),
                ('espacios', djongo.models.fields.EmbeddedField(blank=True, model_container=espacios.models.EspaciosEmbebido, model_form_class=espacios.forms.EspaciosEmbebidoForm, null=True)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'display',
            },
        ),
    ]