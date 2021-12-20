# Generated by Django 3.2.5 on 2021-08-24 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repuesto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repuesto',
            name='clasificacion',
            field=models.CharField(choices=[('Automotriz', 'Automotriz'), ('Ferreteria', 'Ferreteria'), ('Pinturas', 'Pinturas'), ('Rodamientos', 'Rodamientos'), ('Solventes', 'Solventes'), ('Bandas_cadenas', 'Bandas y cadenas'), ('Limpieza', 'Limpieza'), ('Autopartes', 'Autopartes'), ('Sellos_empaques', 'Sellos y empaques'), ('Lubricantes', 'Lubricantes')], default='Sellos_empaques', max_length=20),
        ),
        migrations.AlterField(
            model_name='repuesto',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='repuesto',
            name='imagen',
            field=models.ImageField(upload_to='imagenes/repuestos/'),
        ),
    ]
