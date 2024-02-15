# Generated by Django 5.0 on 2024-02-14 14:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0010_fluxodecaixa_pacienteexame_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solicitacao', models.CharField(choices=[('sim', 'SIM'), ('nao', 'NÃO')], max_length=45)),
                ('data_exame', models.DateField()),
                ('visao_le', models.IntegerField()),
                ('visao_ld', models.IntegerField()),
                ('correcao_visual', models.CharField(choices=[('sim', 'SIM'), ('nao', 'NÃO')], max_length=10)),
                ('campo_visual_le', models.IntegerField()),
                ('campo_visual_ld', models.IntegerField()),
                ('exame_validade', models.DateField()),
                ('conclusao', models.CharField(choices=[('apto', 'APTO'), ('inapto', 'INAPTO')], max_length=10)),
                ('complemento', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(auto_now_add=True)),
                ('valor_pix', models.FloatField(default=0)),
                ('valor_dinheiro', models.FloatField(default=0)),
                ('valor_total', models.FloatField(blank=True, null=True)),
                ('metodo_pagamento', models.CharField(choices=[('PIX', 'PIX'), ('DINHEIRO', 'DINHEIRO'), ('PIX/DINHEIRO', 'PIX/DINHEIRO')], max_length=45)),
            ],
        ),
        migrations.RemoveField(
            model_name='pacienteexame',
            name='paciente',
        ),
        migrations.CreateModel(
            name='Atendimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField()),
                ('id_paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.paciente')),
                ('id_exame', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.exame')),
                ('id_pagamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.pagamento')),
            ],
        ),
        migrations.DeleteModel(
            name='FluxoDeCaixa',
        ),
        migrations.DeleteModel(
            name='PacienteExame',
        ),
    ]
