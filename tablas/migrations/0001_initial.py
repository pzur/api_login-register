# Generated by Django 3.0.2 on 2020-03-22 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('idcli', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=150)),
                ('apellido', models.CharField(max_length=150)),
                ('direccion', models.CharField(max_length=200)),
                ('telefono', models.IntegerField(blank=True, null=True)),
                ('correo', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('foto', models.ImageField(blank=True, upload_to='clientes')),
            ],
        ),
        migrations.CreateModel(
            name='Paseador',
            fields=[
                ('idpas', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=150)),
                ('apellido', models.CharField(max_length=150)),
                ('direccion', models.CharField(max_length=200)),
                ('rating', models.IntegerField()),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.CharField(blank=True, max_length=100, null=True)),
                ('foto', models.ImageField(blank=True, upload_to='paseadores')),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('idmas', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('raza', models.CharField(blank=True, max_length=50, null=True)),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('peso', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('sexo', models.CharField(blank=True, choices=[('macho', 'macho'), ('hembra', 'hembra')], max_length=50, null=True)),
                ('tipo_mascota', models.CharField(blank=True, choices=[('perro', 'perro'), ('gato', 'gato')], max_length=50, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=100, null=True)),
                ('foto', models.ImageField(blank=True, upload_to='mascotas')),
                ('Cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dueño', to='tablas.Cliente')),
                ('pash', models.ManyToManyField(blank=True, to='tablas.Paseador')),
            ],
        ),
    ]
