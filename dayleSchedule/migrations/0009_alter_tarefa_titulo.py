# Generated by Django 3.2.3 on 2022-07-29 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dayleSchedule', '0008_remove_cronograma_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefa',
            name='titulo',
            field=models.CharField(default='Nova Tarefa', max_length=50),
        ),
    ]
