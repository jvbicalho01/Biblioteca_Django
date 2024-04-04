# Generated by Django 5.0.3 on 2024-04-04 17:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0017_alter_emprestimo_data_devolucao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='avaliacao',
            field=models.CharField(blank=True, choices=[('P', 'Péssimo'), ('R', 'Ruim'), ('B', 'Bom'), ('O', 'Ótimo')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='data_emprestimo',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 4, 14, 14, 55, 110010)),
        ),
    ]
