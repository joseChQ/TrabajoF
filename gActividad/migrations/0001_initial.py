# Generated by Django 3.1.1 on 2020-10-08 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gEvento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horaInicio', models.DateTimeField()),
                ('horaFin', models.DateTimeField()),
                ('fechaInicio', models.DateField()),
                ('fechaClausura', models.DateField()),
                ('idSubevento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gEvento.subevento')),
            ],
        ),
        migrations.CreateModel(
            name='Ponente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('informacionAcademica', models.CharField(max_length=30)),
                ('correo', models.EmailField(max_length=50)),
                ('idActividad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gActividad.actividad')),
            ],
        ),
    ]