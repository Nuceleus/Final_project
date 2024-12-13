# Generated by Django 4.2.3 on 2024-12-13 02:47

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
                ('idcliente', models.AutoField(primary_key=True, serialize=False)),
                ('cliente_nombre', models.CharField(max_length=100)),
                ('cliente_email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idproducto', models.AutoField(primary_key=True, serialize=False)),
                ('producto_nombre', models.CharField(max_length=100, verbose_name='producto')),
                ('producto_descripcion', models.TextField(verbose_name='descripción del producto')),
                ('producto_imagen', models.ImageField(blank=True, null=True, upload_to='imagenes/', verbose_name='imagen')),
                ('producto_precio', models.PositiveIntegerField(verbose_name='precio del producto')),
                ('producto_inventario', models.PositiveIntegerField(verbose_name='inventario')),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('idservicio', models.AutoField(primary_key=True, serialize=False)),
                ('servicio_nombre', models.CharField(max_length=100, verbose_name='servicio')),
                ('servicio_descripcion', models.TextField(verbose_name='descripción del servicio')),
                ('servicio_imagen', models.ImageField(blank=True, null=True, upload_to='imagenes/', verbose_name='imagen')),
                ('servicio_precio', models.PositiveIntegerField(verbose_name='precio del servicio')),
            ],
        ),
        migrations.CreateModel(
            name='Vacante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_vacante', models.CharField(default='DEFAULT-0001', max_length=50, unique=True)),
                ('cargo', models.CharField(max_length=100)),
                ('area', models.CharField(choices=[('Sin asignar', 'Sin asignar'), ('Administración', 'Administración'), ('Finanzas', 'Finanzas'), ('Tecnología', 'Tecnología'), ('Recursos Humanos', 'Recursos Humanos'), ('Ventas', 'Ventas')], default='Sin asignar', max_length=100)),
                ('numero_puestos', models.IntegerField(blank=True, default=0, null=True)),
                ('modalidad_trabajo', models.CharField(choices=[('Presencial', 'Presencial'), ('Remoto', 'Remoto'), ('Híbrido', 'Híbrido')], max_length=50)),
                ('tipo_contrato', models.CharField(choices=[('Indefinido', 'Indefinido'), ('Temporal', 'Temporal'), ('Prácticas', 'Prácticas'), ('Freelance', 'Freelance')], max_length=50)),
                ('jornada_trabajo', models.CharField(choices=[('Tiempo completo', 'Tiempo completo'), ('Medio tiempo', 'Medio tiempo'), ('Por horas', 'Por horas')], max_length=50)),
                ('descripcion_vacante', models.TextField(max_length=6000)),
                ('tiempo_experiencia', models.CharField(choices=[('Sin experiencia', 'Sin experiencia'), ('1 año', '1 año'), ('2 años', '2 años'), ('3 años o más', '3 años o más')], max_length=50)),
                ('nivel_estudios', models.CharField(choices=[('Secundaria', 'Secundaria'), ('Técnico', 'Técnico'), ('Tecnólogo', 'Tecnólogo'), ('Profesional', 'Profesional'), ('Postgrado', 'Postgrado')], max_length=50)),
                ('departamento', models.CharField(choices=[('Sin asignar', 'Sin asignar'), ('Antioquia', 'Antioquia'), ('Bogotá', 'Bogotá'), ('Valle del Cauca', 'Valle del Cauca'), ('Cundinamarca', 'Cundinamarca')], default='Sin asignar', max_length=100)),
                ('ciudad', models.CharField(choices=[('Medellín', 'Medellín'), ('Bogotá', 'Bogotá'), ('Cali', 'Cali'), ('Barranquilla', 'Barranquilla')], max_length=100)),
                ('rango_salarial', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_publicacion', models.DateField(auto_now_add=True)),
                ('empresa_usuaria', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('idventa', models.AutoField(primary_key=True, serialize=False)),
                ('venta_fecha', models.DateField()),
                ('venta_total', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('iddetalleventa', models.AutoField(primary_key=True, serialize=False)),
                ('detalle_cantidad', models.PositiveIntegerField()),
                ('detalle_precio', models.PositiveIntegerField()),
                ('idproducto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='proyecto_negocio.producto')),
                ('idservicio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='proyecto_negocio.servicio')),
                ('idventa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto_negocio.venta')),
            ],
        ),
    ]
