# Generated by Django 5.0.6 on 2024-06-07 04:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PaginaWeb', '0011_remove_pedido_usuario_id_pago_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='imagen',
        ),
    ]