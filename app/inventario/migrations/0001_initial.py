# Generated by Django 3.0 on 2019-12-16 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hardware',
            fields=[
                ('codigoactivo', models.IntegerField(db_column='CodigoActivo', max_length=12, primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='Nombre', max_length=30)),
                ('descripcion', models.CharField(db_column='Descripcion', max_length=50)),
                ('modelo', models.CharField(db_column='Modelo', max_length=30)),
                ('estado', models.IntegerField(db_column='Estado')),
            ],
            options={
                'db_table': 'hardware',
                'managed': False,
            },
        ),
    ]
