# Generated by Django 3.2.3 on 2022-07-29 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dayleSchedule', '0005_rename_titulo_cronograma_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='cronograma',
            name='titulo',
            field=models.CharField(default='Novo Cronograma', max_length=100),
        ),
    ]
