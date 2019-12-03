# Generated by Django 2.2.7 on 2019-11-10 17:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Pedido', '0014_auto_20191110_1226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='comentar_status_pedido',
        ),
        migrations.AddField(
            model_name='status',
            name='data_comentario',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data do Comentario'),
        ),
        migrations.AlterField(
            model_name='status',
            name='comentario',
            field=models.TextField(blank=True, null=True, verbose_name='Comentar Status'),
        ),
    ]