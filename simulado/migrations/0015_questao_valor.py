# Generated by Django 4.1 on 2022-08-29 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulado', '0014_alternativa_alter_questao_texto_alter_resposta_texto_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='questao',
            name='valor',
            field=models.IntegerField(default=0),
        ),
    ]
