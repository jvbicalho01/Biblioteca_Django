# Generated by Django 5.0.3 on 2024-04-02 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0012_alter_emprestimo_data_devolução_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emprestimo',
            name='tempo_duracao',
        ),
    ]
