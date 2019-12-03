# Generated by Django 2.2.7 on 2019-11-10 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pedido', '0011_pedido_comentar_status_pedido'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='pagamento',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Boleto Bancário'), (1, 'Cartão de Debíto'), (2, 'Cartão de Credito'), (3, 'Transferencia Bancária')], default=0, verbose_name='Pagamento'),
        ),
    ]
