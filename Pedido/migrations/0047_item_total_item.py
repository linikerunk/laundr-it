# Generated by Django 2.2.7 on 2019-11-23 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pedido', '0046_auto_20191122_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='total_item',
            field=models.DecimalField(decimal_places=2, default=1, editable=False, max_digits=6, verbose_name='Total Item'),
            preserve_default=False,
        ),
    ]
