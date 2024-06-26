# Generated by Django 4.1.2 on 2024-04-23 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PaginaWeb', '0002_pedido_producto_reserva_tipo_usuario_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='medio_pago',
            fields=[
                ('id_pago', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='tipo_usuario',
            name='id_tipo',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='pedido_producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('cod_pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PaginaWeb.pedido')),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PaginaWeb.producto')),
            ],
        ),
    ]
