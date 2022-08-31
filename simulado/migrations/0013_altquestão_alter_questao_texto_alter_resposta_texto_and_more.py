# Generated by Django 4.1 on 2022-08-26 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('simulado', '0012_alternativaq_correta'),
    ]

    operations = [
        migrations.CreateModel(
            name='AltQuestão',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField(verbose_name='texto_alt')),
                ('correta', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='questao',
            name='texto',
            field=models.TextField(verbose_name='texto_quest'),
        ),
        migrations.AlterField(
            model_name='resposta',
            name='texto',
            field=models.TextField(verbose_name='texto_resp'),
        ),
        migrations.DeleteModel(
            name='AlternativaQ',
        ),
        migrations.AddField(
            model_name='altquestão',
            name='questao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simulado.questao'),
        ),
    ]
