# Generated by Django 3.2.3 on 2021-05-20 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vuelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origen', models.CharField(max_length=64)),
                ('destino', models.CharField(max_length=64)),
                ('duracion', models.IntegerField()),
            ],
        ),
    ]
