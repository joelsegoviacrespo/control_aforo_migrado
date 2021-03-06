# Generated by Django 2.2.13 on 2020-08-30 15:56

from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('id_camara_zona', models.CharField(default='', max_length=255)),
                ('mac_wifi', models.CharField(default='', max_length=30)),
                ('descripcion', models.CharField(default='', max_length=300)),
                ('color_barra_cabecera', models.CharField(choices=[('WTH', 'Blanco'), ('G30', 'Gris 30'), ('G60', 'Gris 60'), ('BLK', 'Negro')], default='BLK', max_length=3)),
                ('texto_barra_cabecera', models.CharField(default='', max_length=100)),
                ('logotipo', models.ImageField(blank=True, upload_to='images/')),
                ('logotipo_archivo_nombre', models.CharField(blank=True, default='', max_length=300)),
                ('logotipo_posicion', models.CharField(choices=[('CTR', 'Centro'), ('RGT', 'Derecha'), ('LFT', 'Izquierda')], default='RGT', max_length=3)),
                ('fondo_imagen', models.ImageField(blank=True, upload_to='images/')),
                ('fondo_imagen_archivo_nombre', models.CharField(blank=True, default='', max_length=300)),
                ('aforo_maximo', models.IntegerField(default='0')),
                ('aforo_formato', models.CharField(choices=[('PCT', 'Porcentaje'), ('NMB', 'Número')], default='NMB', max_length=3)),
                ('aforo_mostrar_maximo', models.BooleanField(default=False)),
                ('aforo_mostrar_casi_lleno', models.BooleanField(default=False)),
                ('aforo_frase_verde', models.CharField(blank=True, default='', max_length=150)),
                ('aforo_frase_ambar', models.CharField(blank=True, default='', max_length=150)),
                ('aforo_frase_rojo', models.CharField(blank=True, default='', max_length=150)),
                ('monitor_estado', models.BooleanField(default=True)),
            ],
        ),
    ]
