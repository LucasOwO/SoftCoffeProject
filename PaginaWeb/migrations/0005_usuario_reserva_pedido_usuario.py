# Generated by Django 4.1.2 on 2024-04-23 22:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PaginaWeb', '0004_usuario_tipo_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='usuario_reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_reserva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PaginaWeb.reserva')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PaginaWeb.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='pedido_usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PaginaWeb.pedido')),
                ('id_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PaginaWeb.medio_pago')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PaginaWeb.usuario')),
            ],
        ),
    ]
