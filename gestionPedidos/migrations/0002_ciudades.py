# Generated by Django 3.0.6 on 2020-06-07 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('pais', models.CharField(max_length=30)),
                ('continente', models.CharField(max_length=30)),
            ],
        ),
    ]
