# Generated by Django 2.2.13 on 2021-02-17 14:43

from django.db import migrations
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Streaming',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'streaming',
            },
        ),
    ]
