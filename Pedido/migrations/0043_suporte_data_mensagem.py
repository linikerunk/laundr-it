# Generated by Django 2.2.7 on 2019-11-20 19:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Pedido', '0042_remove_suporte_data_mensagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='suporte',
            name='data_mensagem',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data do Comentario'),
        ),
    ]
