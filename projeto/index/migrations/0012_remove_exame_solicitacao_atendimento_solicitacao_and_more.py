# Generated by Django 5.0 on 2024-02-14 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0011_exame_pagamento_remove_pacienteexame_paciente_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exame',
            name='solicitacao',
        ),
        migrations.AddField(
            model_name='atendimento',
            name='solicitacao',
            field=models.CharField(choices=[('PRIMEIRA_HABILITACAO', 'PRIMEIRA HABILITAÇÃO'), ('RENOVACAO', 'RENOVAÇÃO'), ('RENOVACAO_ATIV_REM', 'RENOVAÇÃO ATIV. REMUNERADA'), ('ADICAO_CATEGORIA', 'ADIÇÃO DE CATEGORIA'), ('MUDANCA_CATEGORIA', 'MUDANÇA DE CATEGORIA'), ('ALTERACAO_DADOS', 'ALTERAÇÃO DE DADOS')], default='PRIMEIRA_HABILITACAO', max_length=45),
        ),
        migrations.AlterField(
            model_name='atendimento',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='exame',
            name='campo_visual_ld',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='exame',
            name='campo_visual_le',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='exame',
            name='conclusao',
            field=models.CharField(blank=True, choices=[('apto', 'APTO'), ('inapto', 'INAPTO')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='exame',
            name='correcao_visual',
            field=models.CharField(blank=True, choices=[('sim', 'SIM'), ('nao', 'NÃO')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='exame',
            name='data_exame',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='exame',
            name='exame_validade',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='exame',
            name='visao_ld',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='exame',
            name='visao_le',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
