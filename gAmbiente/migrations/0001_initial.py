# Generated by Django 3.1.1 on 2020-11-08 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ambiente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=25)),
                ('aforo', models.IntegerField()),
                ('puertasEscape', models.IntegerField()),
                ('visibilidad', models.BooleanField(default=True)),
            ],
        ),
    ]
