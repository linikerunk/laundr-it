# Generated by Django 2.2.7 on 2019-11-10 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Servico', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servico',
            options={'ordering': ('-nome_servico',), 'verbose_name': 'serviço', 'verbose_name_plural': 'serviços'},
        ),
        migrations.RemoveField(
            model_name='servico',
            name='descricao',
        ),
        migrations.AddField(
            model_name='servico',
            name='nome_servico',
            field=models.CharField(default=1, max_length=100, verbose_name='Nome Serviço'),
            preserve_default=False,
        ),
    ]
