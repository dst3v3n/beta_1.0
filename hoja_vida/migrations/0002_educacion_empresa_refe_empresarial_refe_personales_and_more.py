# Generated by Django 4.2.7 on 2023-11-27 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoja_vida', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Educacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Archivo', models.FileField(upload_to='Archivo_Educacion')),
                ('Nombre_Instituto', models.CharField(max_length=50)),
                ('Ano_graduacion', models.DateField()),
                ('Tiempo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_empresa', models.CharField(max_length=50)),
                ('Cargo', models.CharField(max_length=50)),
                ('Fecha_Inicio', models.DateField()),
                ('Fecha_Finalizacion', models.DateField()),
                ('Funciones', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Refe_empresarial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_Empresa', models.CharField(max_length=50)),
                ('Nombre_Jefe', models.CharField(max_length=50)),
                ('Direccion', models.CharField(max_length=50)),
                ('N_celular', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Refe_personales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_person', models.CharField(max_length=50)),
                ('Apellido_person', models.CharField(max_length=50)),
                ('Direccion', models.CharField(max_length=50)),
                ('N_celular', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='informacion_person',
            name='Email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
