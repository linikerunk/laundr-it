# Generated by Django 2.2.6 on 2019-12-02 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pedido', '0047_item_total_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='total_item',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=6, verbose_name='Valor Item'),
        ),
    ]
