# Generated by Django 4.1 on 2022-08-26 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simulado', '0009_rename_alternativa_alternativa_questao'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Alternativa_questao',
            new_name='Alternativa',
        ),
    ]
