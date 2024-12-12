# Generated by Django 4.2.3 on 2024-12-12 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto_negocio', '0002_alter_producto_producto_imagen_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciudad', models.CharField(max_length=100)),
                ('cargo', models.CharField(max_length=100)),
                ('estudios', models.CharField(max_length=100)),
                ('salario', models.IntegerField()),
                ('fecha_publicacion', models.DateField()),
                ('empresa', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='producto',
            name='producto_descripcion',
            field=models.TextField(verbose_name='descripción del producto'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='producto_imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes/', verbose_name='imagen'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='producto_inventario',
            field=models.PositiveIntegerField(verbose_name='inventario'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='producto_nombre',
            field=models.CharField(max_length=100, verbose_name='producto'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='producto_precio',
            field=models.PositiveIntegerField(verbose_name='precio del producto'),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='servicio_descripcion',
            field=models.TextField(verbose_name='descripción del servicio'),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='servicio_imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes/', verbose_name='imagen'),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='servicio_nombre',
            field=models.CharField(max_length=100, verbose_name='servicio'),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='servicio_precio',
            field=models.PositiveIntegerField(verbose_name='precio del servicio'),
        ),
    ]
