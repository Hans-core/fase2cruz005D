# Generated by Django 3.1.3 on 2020-11-03 23:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movie',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('gene', models.CharField(blank=True, choices=[('Accion', 'acc'), ('Terror', 'terr'), ('Horror', 'Horr'), ('Comedia', 'Com'), ('Ficción', 'fic'), ('Otros', 'otro')], default='Otros', max_length=10)),
                ('desc', models.TextField(blank=True, default='', max_length=1000)),
                ('clasif', models.IntegerField()),
                ('imagen', models.ImageField(blank=True, default='media/imagenes/not-found.png', null=True, upload_to='media/imagenes')),
            ],
        ),
    ]
